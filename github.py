from dataclasses import dataclass
from urllib.parse import quote

import requests

from utils import github_api_headers

REQUEST_TIMEOUT_SECONDS = 30


@dataclass
class Asset:
    browser_download_url: str
    name: str


@dataclass
class GithubRelease:
    tag_name: str
    html_url: str
    assets: list[Asset]


@dataclass(frozen=True)
class GithubCommit:
    sha: str
    html_url: str
    subject: str


def _to_github_release(release) -> GithubRelease:
    assets = [
        Asset(browser_download_url=asset["browser_download_url"], name=asset["name"])
        for asset in release["assets"]
    ]

    return GithubRelease(
        tag_name=release["tag_name"], html_url=release["html_url"], assets=assets
    )


def _fetch_release(url: str) -> GithubRelease | None:
    response = requests.get(
        url,
        headers=github_api_headers(),
        timeout=REQUEST_TIMEOUT_SECONDS,
    )

    if response.status_code == 404:
        return None

    response.raise_for_status()
    return _to_github_release(response.json())


def get_release_by_tag(repo_url: str, tag: str) -> GithubRelease | None:
    encoded_tag = quote(tag, safe="")
    url = f"https://api.github.com/repos/{repo_url}/releases/tags/{encoded_tag}"
    return _fetch_release(url)


def get_last_build_version(repo_url: str) -> GithubRelease | None:
    url = f"https://api.github.com/repos/{repo_url}/releases/latest"
    return _fetch_release(url)


def get_commits_between(
    repo_url: str, base: str, head: str
) -> list[GithubCommit] | None:
    url = f"https://api.github.com/repos/{repo_url}/compare/{base}...{head}"
    response = requests.get(
        url,
        headers=github_api_headers(),
        timeout=REQUEST_TIMEOUT_SECONDS,
    )
    if response.status_code == 404:
        return None
    response.raise_for_status()

    payload = response.json()
    if not isinstance(payload, dict):
        raise ValueError("GitHub compare response was not an object")

    commits = payload.get("commits", [])
    if not isinstance(commits, list):
        raise ValueError("GitHub compare response did not contain a commit list")

    result: list[GithubCommit] = []
    for commit in commits:
        if not isinstance(commit, dict):
            continue
        commit_details = commit.get("commit", {})
        if not isinstance(commit_details, dict):
            continue
        message = commit_details.get("message", "")
        sha = commit.get("sha")
        html_url = commit.get("html_url")
        if not isinstance(message, str):
            continue
        if not isinstance(sha, str) or not isinstance(html_url, str):
            continue

        result.append(
            GithubCommit(
                sha=sha,
                html_url=html_url,
                subject=message.partition("\n")[0],
            )
        )

    return result


def get_release_asset_json(
    release: GithubRelease, asset_name: str
) -> list[str] | None:
    asset = next((asset for asset in release.assets if asset.name == asset_name), None)
    if asset is None:
        return None

    # This is a browser download URL, not an API endpoint; do not send the
    # GitHub token to it (or to any redirect target).
    response = requests.get(
        asset.browser_download_url,
        headers={"Accept": "application/octet-stream"},
        timeout=REQUEST_TIMEOUT_SECONDS,
    )
    response.raise_for_status()

    contents = response.json()
    if not isinstance(contents, list) or not all(
        isinstance(patch, str) for patch in contents
    ):
        raise ValueError(f"Release asset {asset_name} must contain a list of strings")

    return contents
