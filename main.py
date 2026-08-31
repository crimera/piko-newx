from argparse import ArgumentParser
from datetime import datetime, timezone
import json
from pathlib import Path

import apkmirror
import github
from apkmirror import Version
from build_piko import PIKO_REPO, PikoBuild, build_piko_patches
from build_variants import get_xlite_patches
from constants import REPO
from download_bins import download_morphe_cli
from utils import publish_release, sign_artifact


CHANGELOG_FILE = "CHANGELOG.md"
PATCHES_LIST_ASSET = "patches-list.json"
PATCHES_MPP = "bins/patches.mpp"


def get_latest_version(
    versions: list[Version], supported_versions: frozenset[str] | None = None
) -> Version | None:
    for version in versions:
        if supported_versions is None or version.version in supported_versions:
            return version


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
    previous_release: github.GithubRelease | None, current_commit: str
) -> list[github.GithubCommit] | None:
    if previous_release is None:
        return None

    previous_commit = previous_release.tag_name.rsplit("-", maxsplit=1)[-1]
    if previous_commit == current_commit[:7]:
        return []

    return github.get_commits_between(PIKO_REPO, previous_commit, current_commit)


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
    repo: str = REPO,
) -> None:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    heading = f"# [{version}](https://github.com/{repo}/releases/tag/{tag}) ({today})"

    sections: list[str] = []

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
    previous_release: github.GithubRelease | None = None,
):
    piko_commit = piko_build.commit[:7]
    release_tag = f"{latest_version.version}-{piko_commit}"

    download_morphe_cli(include_prereleases=True)

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
    commits = get_piko_commits(previous_release, piko_build.commit)

    update_changelog(
        version=release_tag,
        tag=release_tag,
        new_patches=new_patches,
        commits=commits,
    )

    patch_list = format_new_patch_list(new_patches)
    commit_list = format_commit_list(commits)
    release_sections = [section for section in (commit_list, patch_list) if section]
    additional_notes = "\n\n".join(release_sections)
    additional_notes = f"{additional_notes}\n\n" if additional_notes else ""
    message = f"""{additional_notes}Piko source:
[x-lite@{piko_commit}](https://github.com/crimera/piko/commit/{piko_build.commit})
"""

    signature = sign_artifact(PATCHES_MPP)
    release_assets = [PATCHES_MPP, PATCHES_LIST_ASSET, *( [signature] if signature else [] )]

    publish_release(
        release_tag,
        release_assets,
        message,
        release_tag,
    )


def main():
    versions = apkmirror.get_versions(
        "https://www.apkmirror.com/apk/x-corp/twitter/"
    )

    # Build the same Piko revision that will be used for patching first.  Its
    # compatibility targets determine which X APK can actually be patched.
    piko_build = build_piko_patches()
    latest_version = get_latest_version(versions, piko_build.supported_versions)
    if latest_version is None:
        raise Exception("No X version is supported by the Piko x-lite patches")

    release_tag = f"{latest_version.version}-{piko_build.commit[:7]}"
    last_build_version: github.GithubRelease | None = github.get_last_build_version(REPO)
    if (
        last_build_version is not None
        and last_build_version.tag_name == release_tag
    ):
        print("No new compatible version found")
        return

    print(f"New compatible version found: {latest_version.version}")
    process(latest_version, piko_build, last_build_version)


def manual(version: str):
    piko_build = build_piko_patches()
    if version not in piko_build.supported_versions:
        supported = ", ".join(sorted(piko_build.supported_versions))
        raise ValueError(f"{version} is not supported by Piko x-lite (supported: {supported})")

    link = (
        "https://www.apkmirror.com/apk/x-corp/twitter/"
        f"x-{version.replace('.', '-')}-release"
    )
    process(
        Version(link=link, version=version),
        piko_build,
        github.get_last_build_version(REPO),
    )


if __name__ == "__main__":
    parser = ArgumentParser(description="Piko APK")
    parser.add_argument("--m", action="store", dest="mode", default=0)
    parser.add_argument("--v", action="store", dest="version", default=0)
    args = parser.parse_args()

    if args.mode:
        if not args.version:
            raise Exception("Version is required.")
        manual(args.version)
    else:
        main()
