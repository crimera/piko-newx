from argparse import ArgumentParser
from datetime import datetime, timezone
import json
from pathlib import Path
import re

import apkmirror
import github
from apkmirror import Version
from build_piko import PIKO_REPO, PikoBuild, build_piko_patches
from build_variants import get_xlite_patches
from constants import REPO
from download_bins import download_morphe_cli
from utils import publish_release, sign_artifact


CHANGELOG_FILE = "CHANGELOG.md"
PATCHES_BUNDLE_FILE = "patches-bundle.json"
PATCHES_LIST_ASSET = "patches-list.json"
PATCHES_MPP = "bins/patches.mpp"
RELEASE_TAG_PATTERN = re.compile(r"^v\d+\.\d+\.\d+$")
LEGACY_RELEASE_PATTERN = re.compile(r"^(?P<app>.+)-(?P<piko>[0-9a-f]{7,40})$")


def get_latest_version(
    versions: list[Version], supported_versions: frozenset[str] | None = None
) -> Version | None:
    for version in versions:
        if supported_versions is None or version.version in supported_versions:
            return version


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
    latest_version: Version,
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
        previous_app_version != latest_version.version
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
    latest_version: Version,
    piko_build: PikoBuild,
    repo: str = REPO,
) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    metadata = {
        "version": release_tag,
        "download_url": f"https://github.com/{repo}/releases/download/{release_tag}/patches.mpp",
        "created_at": now,
        "description": f"Piko x-lite patch bundle for Morphe ({release_tag}).",
        "signature_download_url": f"https://github.com/{repo}/releases/download/{release_tag}/patches.mpp.asc",
        "app_version": latest_version.version,
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


def get_piko_commits(
    previous_release: github.GithubRelease | None,
    previous_piko_commit: str | None,
    current_commit: str,
) -> list[github.GithubCommit] | None:
    if previous_release is None or previous_piko_commit is None:
        return None

    if current_commit.startswith(previous_piko_commit):
        return []

    return github.get_commits_between(PIKO_REPO, previous_piko_commit, current_commit)


def format_commit_list(commits: list[github.GithubCommit] | None) -> str:
    if not commits:
        return ""

    entries = "\n".join(
        f"- [`{commit.sha[:7]}`]({commit.html_url}) {commit.subject}"
        for commit in commits
    )
    return f"Piko commits since previous release:\n{entries}"


def update_changelog(
    version: str,
    tag: str,
    new_patches: list[str],
    commits: list[github.GithubCommit] | None,
    generated_changelog: str = "",
    repo: str = REPO,
) -> None:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    heading = f"# [{version}](https://github.com/{repo}/releases/tag/{tag}) ({today})"

    sections: list[str] = []

    if generated_changelog:
        sections.append(generated_changelog)

    if commits:
        commit_bullets = "\n".join(
            f"* [`{commit.sha[:7]}`]({commit.html_url}) {commit.subject}"
            for commit in commits
        )
        sections.append(f"### Commits\n{commit_bullets}")

    if new_patches:
        patch_bullets = "\n".join(f"* **Twitter:** {patch}" for patch in new_patches)
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
    latest_version: Version,
    piko_build: PikoBuild,
    release_tag: str,
    previous_release: github.GithubRelease | None = None,
    previous_piko_commit: str | None = None,
    generated_changelog: str = "",
) -> None:
    piko_commit = piko_build.commit[:7]

    download_morphe_cli(include_prereleases=False)

    print(f"Using Piko x-lite@{piko_commit}")
    patches = get_xlite_patches("bins/morphe-cli.jar", PATCHES_MPP)
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
    commits = get_piko_commits(
        previous_release, previous_piko_commit, piko_build.commit
    )

    update_changelog(
        version=release_tag,
        tag=release_tag,
        new_patches=new_patches,
        commits=commits,
        generated_changelog=generated_changelog,
    )

    patch_list = format_new_patch_list(new_patches)
    commit_list = format_commit_list(commits)
    release_sections = [
        section for section in (generated_changelog, commit_list, patch_list) if section
    ]
    additional_notes = "\n\n".join(release_sections)
    additional_notes = f"{additional_notes}\n\n" if additional_notes else ""
    message = f"""{additional_notes}Piko source:
[x-lite@{piko_commit}](https://github.com/crimera/piko/commit/{piko_build.commit})
X app version: `{latest_version.version}`
Release version: `{release_tag}`
"""

    signature = sign_artifact(PATCHES_MPP)
    release_assets = [PATCHES_MPP, PATCHES_LIST_ASSET, *( [signature] if signature else [] )]

    publish_release(
        release_tag,
        release_assets,
        message,
        release_tag,
    )
    write_patches_bundle(release_tag, latest_version, piko_build)


def should_publish(
    latest_version: Version,
    piko_build: PikoBuild,
    previous_release: github.GithubRelease | None,
    semantic_bump: bool,
    metadata: dict[str, str],
) -> bool:
    if semantic_bump:
        return True

    return has_release_content_changed(
        latest_version, piko_build, previous_release, metadata
    )


def main(
    release_tag: str,
    semantic_bump: bool,
    generated_changelog: str = "",
) -> None:
    patch_version = validate_release_tag(release_tag)
    versions = apkmirror.get_versions(
        "https://www.apkmirror.com/apk/x-corp/twitter/"
    )

    # Build the same Piko revision that will be used for patching first.  Its
    # compatibility targets determine which X APK can actually be patched.
    piko_build = build_piko_patches(patch_version=patch_version)
    latest_version = get_latest_version(versions, piko_build.supported_versions)
    if latest_version is None:
        raise Exception("No X version is supported by the Piko x-lite patches")

    previous_release = github.get_last_build_version(REPO)
    metadata = read_release_metadata()
    _, previous_piko_commit = get_previous_release_context(
        previous_release, metadata
    )
    if not should_publish(
        latest_version, piko_build, previous_release, semantic_bump, metadata
    ):
        print("No semantic or release-content changes found")
        return

    print(f"Publishing {release_tag} for X {latest_version.version}")
    process(
        latest_version,
        piko_build,
        release_tag=release_tag,
        previous_release=previous_release,
        previous_piko_commit=previous_piko_commit,
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

    latest_version = Version(
        link=(
            "https://www.apkmirror.com/apk/x-corp/twitter/"
            f"x-{version.replace('.', '-')}-release"
        ),
        version=version,
    )
    previous_release = github.get_last_build_version(REPO)
    metadata = read_release_metadata()
    _, previous_piko_commit = get_previous_release_context(
        previous_release, metadata
    )
    if not should_publish(
        latest_version, piko_build, previous_release, semantic_bump, metadata
    ):
        print("No semantic or release-content changes found")
        return

    process(
        latest_version,
        piko_build,
        release_tag=release_tag,
        previous_release=previous_release,
        previous_piko_commit=previous_piko_commit,
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
