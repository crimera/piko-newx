from argparse import ArgumentParser
from datetime import datetime, timezone
import json
from pathlib import Path
import re

import github
from build_piko import PikoBuild, build_piko_patches
from build_variants import get_xlite_patches
from constants import REPO
from download_bins import download_morphe_cli
from utils import publish_release, sign_artifact


CHANGELOG_FILE = "CHANGELOG.md"
CHANGELOG_APP_NAME = "Twitter"
PATCHES_BUNDLE_FILE = "patches-bundle.json"
PATCHES_LIST_ASSET = "patches-list.json"
PATCHES_MPP_DIR = "bins"
RELEASE_TAG_PATTERN = re.compile(r"^v\d+\.\d+\.\d+$")
LEGACY_RELEASE_PATTERN = re.compile(r"^(?P<app>.+)-(?P<piko>[0-9a-f]{7,40})$")
APP_VERSION_PATTERN = re.compile(
    r"^(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)"
    r"(?:-(?P<channel>alpha|beta|prod)\.(?P<revision>\d+))?$"
)
APP_VERSION_CHANNEL_PRIORITY = {"alpha": 0, "beta": 1, "prod": 2}


def app_version_sort_key(version: str) -> tuple[int, int, int, int, int]:
    match = APP_VERSION_PATTERN.fullmatch(version)
    if match is None:
        raise ValueError(f"Unsupported X app version format: {version}")

    channel = match.group("channel")
    channel_priority = (
        APP_VERSION_CHANNEL_PRIORITY[channel] if channel is not None else 3
    )
    revision = int(match.group("revision") or 0)
    return (
        int(match.group("major")),
        int(match.group("minor")),
        int(match.group("patch")),
        channel_priority,
        revision,
    )


def get_latest_version(supported_versions: frozenset[str]) -> str | None:
    if not supported_versions:
        return None

    return max(supported_versions, key=app_version_sort_key)


def validate_release_tag(release_tag: str) -> str:
    if not RELEASE_TAG_PATTERN.fullmatch(release_tag):
        raise ValueError(f"Invalid semantic release tag: {release_tag}")
    return release_tag.removeprefix("v")


def read_release_metadata() -> dict[str, str]:
    metadata_path = Path(PATCHES_BUNDLE_FILE)
    if not metadata_path.exists():
        return {}

    contents = json.loads(metadata_path.read_text(encoding="utf-8"))
    if not isinstance(contents, dict):
        raise ValueError(f"{PATCHES_BUNDLE_FILE} must contain a JSON object")

    return {
        key: value
        for key, value in contents.items()
        if isinstance(key, str) and isinstance(value, str)
    }


def get_legacy_release_context(
    previous_release: github.GithubRelease | None,
) -> tuple[str | None, str | None]:
    if previous_release is None:
        return None, None

    match = LEGACY_RELEASE_PATTERN.fullmatch(previous_release.tag_name)
    if match is None:
        return None, None

    return match.group("app"), match.group("piko")


def get_previous_release_context(
    previous_release: github.GithubRelease | None,
    metadata: dict[str, str],
) -> tuple[str | None, str | None]:
    legacy_app_version, legacy_piko_commit = get_legacy_release_context(previous_release)
    app_version = metadata.get("app_version") or legacy_app_version
    piko_commit = metadata.get("piko_commit") or legacy_piko_commit
    return app_version, piko_commit


def has_release_content_changed(
    app_version: str,
    piko_build: PikoBuild,
    previous_release: github.GithubRelease | None,
    metadata: dict[str, str],
) -> bool:
    if previous_release is None:
        return True

    previous_app_version, previous_piko_commit = get_previous_release_context(
        previous_release, metadata
    )
    if previous_app_version is None or previous_piko_commit is None:
        return True

    return (
        previous_app_version != app_version
        or not piko_build.commit.startswith(previous_piko_commit)
    )


def read_generated_changelog(path: str | None) -> str:
    if path is None:
        return ""

    changelog = Path(path).read_text(encoding="utf-8").strip()
    if changelog == "*No notable changes in this release.*":
        return ""
    return changelog


def write_patches_bundle(
    release_tag: str,
    app_version: str,
    piko_build: PikoBuild,
    repo: str = REPO,
) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    patch_version = validate_release_tag(release_tag)
    mpp_filename = f"patches-{patch_version}.mpp"
    metadata = {
        "version": release_tag,
        "download_url": f"https://github.com/{repo}/releases/download/{release_tag}/{mpp_filename}",
        "created_at": now,
        "description": f"Piko x-lite patch bundle for Morphe ({release_tag}).",
        "signature_download_url": f"https://github.com/{repo}/releases/download/{release_tag}/{mpp_filename}.asc",
        "app_version": app_version,
        "piko_commit": piko_build.commit,
    }
    Path(PATCHES_BUNDLE_FILE).write_text(
        json.dumps(metadata, indent=2) + "\n",
        encoding="utf-8",
    )


def format_new_patch_list(patches: list[str]) -> str:
    if not patches:
        return ""

    entries = "\n".join(f"- {patch}" for patch in patches)
    return f"New patches:\n{entries}"


def write_patches_list(patches: list[str]) -> None:
    Path(PATCHES_LIST_ASSET).write_text(
        json.dumps(patches, indent=2) + "\n",
        encoding="utf-8",
    )


def update_changelog(
    version: str,
    tag: str,
    new_patches: list[str],
    generated_changelog: str = "",
    repo: str = REPO,
    previous_tag: str | None = None,
) -> None:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    display_version = version.removeprefix("v")
    release_url = (
        f"https://github.com/{repo}/compare/{previous_tag}...{tag}"
        if previous_tag is not None
        else f"https://github.com/{repo}/releases/tag/{tag}"
    )
    heading = f"## [{display_version}]({release_url}) ({today})"

    sections: list[str] = []

    if generated_changelog:
        sections.append(generated_changelog)

    if new_patches:
        patch_bullets = "\n".join(
            f"* **{CHANGELOG_APP_NAME}:** {patch}" for patch in new_patches
        )
        sections.append(f"### New Patches\n{patch_bullets}")

    body = "\n\n".join(sections) if sections else "* No new patches or commits."
    entry = f"{heading}\n\n{body}\n\n"

    changelog_path = Path(CHANGELOG_FILE)
    existing = (
        changelog_path.read_text(encoding="utf-8")
        if changelog_path.exists()
        else ""
    )

    if heading not in existing:
        changelog_path.write_text(entry + existing, encoding="utf-8")


def process(
    app_version: str,
    piko_build: PikoBuild,
    release_tag: str,
    previous_release: github.GithubRelease | None = None,
    generated_changelog: str = "",
) -> None:
    piko_commit = piko_build.commit[:7]
    patch_version = validate_release_tag(release_tag)
    patches_mpp = f"{PATCHES_MPP_DIR}/patches-{patch_version}.mpp"

    download_morphe_cli(include_prereleases=False)

    print(f"Using Piko x-lite@{piko_commit}")
    patches = get_xlite_patches("bins/morphe-cli.jar", patches_mpp)
    write_patches_list(patches)

    previous_patches = (
        github.get_release_asset_json(previous_release, PATCHES_LIST_ASSET)
        if previous_release is not None
        else None
    )
    new_patches = (
        [p for p in patches if p not in set(previous_patches)]
        if previous_patches is not None
        else patches
    )
    update_changelog(
        version=release_tag,
        tag=release_tag,
        new_patches=new_patches,
        generated_changelog=generated_changelog,
        previous_tag=previous_release.tag_name if previous_release else None,
    )

    patch_list = format_new_patch_list(new_patches)
    release_sections = [
        section for section in (generated_changelog, patch_list) if section
    ]
    message = "\n\n".join(release_sections)

    signature = sign_artifact(patches_mpp)
    release_assets = [patches_mpp, PATCHES_LIST_ASSET, *( [signature] if signature else [] )]

    publish_release(
        release_tag,
        release_assets,
        message,
        release_tag,
    )
    write_patches_bundle(release_tag, app_version, piko_build)


def should_publish(
    app_version: str,
    piko_build: PikoBuild,
    previous_release: github.GithubRelease | None,
    semantic_bump: bool,
    metadata: dict[str, str],
) -> bool:
    if semantic_bump:
        return True

    return has_release_content_changed(
        app_version, piko_build, previous_release, metadata
    )


def main(
    release_tag: str,
    semantic_bump: bool,
    generated_changelog: str = "",
) -> None:
    patch_version = validate_release_tag(release_tag)

    # Build the same Piko revision that will be used for patching first.  Its
    # compatibility targets determine which X app version is represented.
    piko_build = build_piko_patches(patch_version=patch_version)
    app_version = get_latest_version(piko_build.supported_versions)
    if app_version is None:
        raise Exception("No X version is supported by the Piko x-lite patches")

    previous_release = github.get_last_build_version(REPO)
    metadata = read_release_metadata()
    if not should_publish(
        app_version, piko_build, previous_release, semantic_bump, metadata
    ):
        print("No semantic or release-content changes found")
        return

    print(f"Publishing {release_tag} for X {app_version}")
    process(
        app_version,
        piko_build,
        release_tag=release_tag,
        previous_release=previous_release,
        generated_changelog=generated_changelog,
    )


def manual(
    version: str,
    release_tag: str,
    semantic_bump: bool,
    generated_changelog: str = "",
) -> None:
    patch_version = validate_release_tag(release_tag)
    piko_build = build_piko_patches(patch_version=patch_version)
    if version not in piko_build.supported_versions:
        supported = ", ".join(sorted(piko_build.supported_versions))
        raise ValueError(f"{version} is not supported by Piko x-lite (supported: {supported})")

    previous_release = github.get_last_build_version(REPO)
    metadata = read_release_metadata()
    if not should_publish(
        version, piko_build, previous_release, semantic_bump, metadata
    ):
        print("No semantic or release-content changes found")
        return

    process(
        version,
        piko_build,
        release_tag=release_tag,
        previous_release=previous_release,
        generated_changelog=generated_changelog,
    )


if __name__ == "__main__":
    parser = ArgumentParser(description="Piko APK")
    parser.add_argument("--m", action="store", dest="mode", default=0)
    parser.add_argument("--v", action="store", dest="version", default=0)
    parser.add_argument("--release-tag", required=True)
    parser.add_argument(
        "--semantic-bump", choices=("true", "false"), default="false"
    )
    parser.add_argument("--changelog-file", default=None)
    args = parser.parse_args()

    generated_changelog = read_generated_changelog(args.changelog_file)
    semantic_bump = args.semantic_bump == "true"

    if args.mode:
        if not args.version:
            raise Exception("Version is required.")
        manual(
            args.version,
            args.release_tag,
            semantic_bump,
            generated_changelog,
        )
    else:
        main(args.release_tag, semantic_bump, generated_changelog)
