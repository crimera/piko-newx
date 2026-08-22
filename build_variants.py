import re
import subprocess

from apkmirror import Version
from utils import patch_apk


XLITE_PATCH_NAME = re.compile(r"^Name:\s*(NewX:\s*.+?)\s*$", re.MULTILINE)


def get_xlite_patches(cli: str, patches: str) -> list[str]:
    result = subprocess.run(
        [
            "java",
            "-jar",
            cli,
            "list-patches",
            "--patches",
            patches,
            "--with-descriptions=false",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    output = result.stdout + result.stderr
    includes = list(dict.fromkeys(XLITE_PATCH_NAME.findall(output)))
    if not includes:
        raise RuntimeError("Morphe returned no NewX patches")
    return includes


def build_apks(latest_version: Version, apk: str, piko_commit: str) -> list[str]:
    patches = "bins/patches.mpp"
    cli = "bins/morphe-cli.jar"
    includes = get_xlite_patches(cli, patches)

    patch_apk(
        cli,
        patches,
        apk,
        includes=includes,
        excludes=[],
        out=f"piko-lite-v{latest_version.version}-{piko_commit[:7]}.apk",
        minimum_patches=len(includes),
    )

    return includes
