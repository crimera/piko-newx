import os
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

PIKO_REPO = "crimera/piko"
PIKO_REPOSITORY = f"https://github.com/{PIKO_REPO}.git"
PIKO_BRANCH = "x-lite"
XLITE_CONSTANTS = (
    "patches/src/main/kotlin/app/crimera/patches/xlite/utils/Constants.kt"
)


@dataclass(frozen=True)
class PikoBuild:
    commit: str
    supported_versions: frozenset[str]


def get_supported_versions(constants: str) -> frozenset[str]:
    """Return the X-Lite app versions supported by the checked-out Piko source."""
    versions = frozenset(
        re.findall(r'AppTarget\(version\s*=\s*"([^"]+)"\)', constants)
    )
    if not versions:
        raise ValueError("Could not find X-Lite compatible app versions in Piko")
    return versions


def build_piko_patches(output: str = "bins/patches.mpp") -> PikoBuild:
    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="piko-") as temporary_directory:
        piko_directory = Path(temporary_directory) / "piko"

        subprocess.run(
            [
                "git",
                "clone",
                "--depth",
                "1",
                "--branch",
                PIKO_BRANCH,
                PIKO_REPOSITORY,
                str(piko_directory),
            ],
            check=True,
        )

        supported_versions = get_supported_versions(
            (piko_directory / XLITE_CONSTANTS).read_text()
        )

        subprocess.run(
            ["./gradlew", "clean", "buildAndroid"],
            cwd=piko_directory,
            env=os.environ.copy(),
            check=True,
        )

        artifacts = sorted(
            (piko_directory / "patches" / "build" / "libs").glob("patches-*.mpp")
        )
        if not artifacts:
            raise FileNotFoundError("Piko did not produce a patches .mpp artifact")

        shutil.copy2(artifacts[-1], output_path)

        commit = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=piko_directory,
            check=True,
            capture_output=True,
            text=True,
        )

    return PikoBuild(commit=commit.stdout.strip(), supported_versions=supported_versions)
