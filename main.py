from apkmirror import Version, Variant
from build_variants import build_apks
from build_piko import build_piko_patches
from download_bins import download_morphe_cli
import github
from utils import panic, publish_release, report_to_telegram
from constants import REPO
import apkmirror
import os
import argparse


def get_latest_release(versions: list[Version]) -> Version | None:
    for i in versions:
        if i.version.find("release") >= 0:
            return i


def process(latest_version: Version):
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

    apkmirror.download_apk(download_link)
    if not os.path.exists("big_file.apkm"):
        panic("Failed to download apkm")

    # Morphe handles .apkm bundles directly; no APKEditor merge is needed.
    download_morphe_cli(include_prereleases=True)

    print("Building Piko patches from the x-lite branch")
    piko_commit = build_piko_patches()

    message: str = f"""
Piko source:
[x-lite@{piko_commit[:7]}](https://github.com/crimera/piko/commit/{piko_commit})
"""

    build_apks(latest_version)

    publish_release(
        latest_version.version,
        [f"piko-lite-v{latest_version.version}.apk"],
        message,
        latest_version.version
    )

    report_to_telegram(tag=latest_version.version)


def main():
    # get latest version
    url: str = "https://www.apkmirror.com/apk/x-corp/twitter/"
    repo_url: str = REPO

    versions = apkmirror.get_versions(url)

    latest_version = get_latest_release(versions)
    if latest_version is None:
        raise Exception("Could not find the latest version")

    # only continue if it's a release
    if latest_version.version.find("release") < 0:
        panic("Latest version is not a release version")

    last_build_version: github.GithubRelease | None = github.get_last_build_version(
        repo_url
    )

    if last_build_version is None:
        panic("Failed to fetch the latest build version")
        return

    # Begin stuff
    if last_build_version.tag_name != latest_version.version:
        print(f"New version found: {latest_version.version}")
    else:
        print("No new version found")
        return

    process(latest_version)


def manual(version:str):
    link = f'https://www.apkmirror.com/apk/x-corp/twitter/x-{version.replace(".","-")}-release'
    latest_version = Version(link=link,version=version)
    process(latest_version)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Piko APK')
    # 0 = auto; 1 = manual;
    parser.add_argument('--m', action="store", dest='mode', default=0)
    parser.add_argument('--v', action="store", dest='version', default=0)

    args = parser.parse_args()
    mode = args.mode

    if not mode: # auto
        main()
    else: # manual
        version = args.version
        if not version:
            raise Exception("Version is required.")
        manual(version)
