from argparse import ArgumentParser
import os

import apkmirror
import github
from apkmirror import Variant, Version
from build_piko import PikoBuild, build_piko_patches
from build_variants import build_apks
from constants import REPO
from download_bins import download_morphe_cli
from utils import panic, publish_release


def get_latest_release(
    versions: list[Version], supported_versions: frozenset[str] | None = None
) -> Version | None:
    for version in versions:
        if "release" not in version.version:
            continue
        if supported_versions is None or version.version in supported_versions:
            return version


def process(latest_version: Version, piko_build: PikoBuild):
    variants: list[Variant] = apkmirror.get_variants(latest_version)

    download_link = next(
        (
            variant
            for variant in variants
            if variant.is_bundle and variant.architecture == "universal"
        ),
        None,
    )
    if download_link is None:
        raise Exception("Universal bundle not found")

    # Keep the input version-specific so a retry cannot accidentally patch a
    # stale APK left by an earlier build.
    apk_path = f"big_file-{latest_version.version}.apkm"
    apkmirror.download_apk(download_link, path=apk_path)
    if not os.path.exists(apk_path):
        panic("Failed to download apkm")

    download_morphe_cli(include_prereleases=True)

    piko_commit = piko_build.commit[:7]
    release_tag = f"{latest_version.version}-{piko_commit}"
    apk_name = f"piko-lite-v{latest_version.version}-{piko_commit}.apk"

    print(f"Using Piko x-lite@{piko_commit}")
    build_apks(latest_version, apk_path, piko_build.commit)

    message = f"""
Piko source:
[x-lite@{piko_commit}](https://github.com/crimera/piko/commit/{piko_build.commit})
"""

    publish_release(
        release_tag,
        [apk_name],
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
    latest_version = get_latest_release(versions, piko_build.supported_versions)
    if latest_version is None:
        raise Exception("No X release is supported by the Piko x-lite patches")

    release_tag = f"{latest_version.version}-{piko_build.commit[:7]}"
    last_build_version: github.GithubRelease | None = github.get_last_build_version(REPO)
    if (
        last_build_version is not None
        and last_build_version.tag_name == release_tag
    ):
        print("No new compatible version found")
        return

    print(f"New compatible version found: {latest_version.version}")
    process(latest_version, piko_build)


def manual(version: str):
    piko_build = build_piko_patches()
    if version not in piko_build.supported_versions:
        supported = ", ".join(sorted(piko_build.supported_versions))
        raise ValueError(f"{version} is not supported by Piko x-lite (supported: {supported})")

    link = (
        "https://www.apkmirror.com/apk/x-corp/twitter/"
        f"x-{version.replace('.', '-')}-release"
    )
    process(Version(link=link, version=version), piko_build)


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
