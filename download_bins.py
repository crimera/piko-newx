import re

import requests

from utils import download, github_api_headers


def download_release_asset(
    repo: str,
    regex: str,
    out_dir: str,
    filename=None,
    include_prereleases: bool = False,
    version=None,
):
    url = f"https://api.github.com/repos/{repo}/releases"

    response = requests.get(
        url,
        headers=github_api_headers(),
        timeout=30,
    )
    if response.status_code != 200:
        remaining = response.headers.get("x-ratelimit-remaining")
        reset = response.headers.get("x-ratelimit-reset")
        detail = (
            f" (remaining={remaining}, reset={reset})"
            if remaining is not None
            else ""
        )
        raise Exception(
            f"Failed to fetch GitHub releases: {response.status_code}{detail}"
        )

    releases = [r for r in response.json() if include_prereleases or not r["prerelease"]]

    if not releases:
        raise Exception(f"No releases found for {repo}")

    if version is not None:
        releases = [r for r in releases if r["tag_name"] == version]

    if not releases:
        raise Exception(f"No release found for version {version}")

    latest_release = releases[0]

    link = None
    for asset in latest_release["assets"]:
        name = asset["name"]
        if re.search(regex, name):
            link = asset["browser_download_url"]
            if filename is None:
                filename = name
            break

    if link is None:
        raise Exception(f"Failed to find asset matching {regex} on release {latest_release['tag_name']}")

    download(link, f"{out_dir.lstrip('/')}/{filename}")

    return latest_release


def download_morphe_cli(include_prereleases: bool = False):
    print("Downloading morphe cli")
    download_release_asset(
        "MorpheApp/morphe-desktop",
        r"^morphe-desktop-.*-all\.jar$",
        "bins",
        "morphe-cli.jar",
        include_prereleases=include_prereleases,
    )
