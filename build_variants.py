from apkmirror import Version
from utils import patch_apk


def build_apks(latest_version: Version, apk: str):
    # patch
    patches = "bins/patches.mpp"
    cli = "bins/morphe-cli.jar"

    includes = [
        "X-Lite: Remove ads",
        "X-Lite: Disable automatic timeline refresh",
        "X-Lite: Restore timeline position",
        "X-Lite: Customize inline actions",
        "X-Lite: Unlock downloads",
        "X-Lite: Hide new-post pill",
    ]

    patch_apk(
        cli,
        patches,
        apk,
        includes=includes,
        excludes=[],
        out=f"piko-lite-v{latest_version.version}.apk",
        minimum_patches=len(includes),
    )
