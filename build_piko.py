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
    "patches/src/main/kotlin/app/crimera/patches/newx/utils/Constants.kt"
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


def pre_build_cleanup(piko_directory: Path) -> None:
    """Remove Instagram, Twitter, and legacy patches/extensions before building."""
    # Remove non-NewX patch source packages
    for path in [
        piko_directory / "patches/src/main/kotlin/app/crimera/patches/instagram",
        piko_directory / "patches/src/main/kotlin/app/crimera/patches/twitter",
        piko_directory / "patches/src/main/kotlin/app/revanced",
    ]:
        if path.exists():
            shutil.rmtree(path)

    # Remove non-NewX extension modules
    for path in [
        piko_directory / "extensions/instagram",
        piko_directory / "extensions/twitter",
    ]:
        if path.exists():
            shutil.rmtree(path)

    # Keep twitter/bringbacktwitter assets for Bring back twitter patch
    twitter_res = piko_directory / "patches/src/main/resources/twitter"
    if twitter_res.exists():
        for item in twitter_res.iterdir():
            if item.name != "bringbacktwitter":
                if item.is_dir():
                    shutil.rmtree(item)
                else:
                    item.unlink()

    addresources_dir = piko_directory / "patches/src/main/resources/addresources"
    if addresources_dir.exists():
        for res_name in ("instagram", "twitter"):
            for matched in addresources_dir.glob(f"*/{res_name}"):
                if matched.is_dir():
                    shutil.rmtree(matched)


def set_project_version(piko_directory: Path, version: str) -> None:
    """Set the version only in the temporary Piko checkout used for a build."""
    properties_path = piko_directory / "gradle.properties"
    lines = properties_path.read_text(encoding="utf-8").splitlines(keepends=True)
    version_indexes = [
        index
        for index, line in enumerate(lines)
        if re.match(r"^\s*version\s*=", line)
    ]
    if len(version_indexes) != 1:
        raise ValueError("Piko gradle.properties must contain exactly one version")

    lines[version_indexes[0]] = f"version = {version}\n"
    properties_path.write_text("".join(lines), encoding="utf-8")


def build_piko_patches(
    output: str = "bins/patches.mpp", patch_version: str | None = None
) -> PikoBuild:
    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if patch_version is not None and patch_version.startswith("v"):
        raise ValueError("patch_version must not include the leading v")

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

        pre_build_cleanup(piko_directory)

        if patch_version is not None:
            set_project_version(piko_directory, patch_version)

        subprocess.run(
            ["./gradlew", "clean", "buildAndroid"],
            cwd=piko_directory,
            env=os.environ.copy(),
            check=True,
        )

        artifacts_directory = piko_directory / "patches" / "build" / "libs"
        if patch_version is not None:
            artifact = artifacts_directory / f"patches-{patch_version}.mpp"
            if not artifact.is_file():
                raise FileNotFoundError(
                    f"Piko did not produce the expected artifact {artifact.name}"
                )
        else:
            artifacts = sorted(artifacts_directory.glob("patches-*.mpp"))
            if not artifacts:
                raise FileNotFoundError("Piko did not produce a patches .mpp artifact")
            artifact = artifacts[-1]

        shutil.copy2(artifact, output_path)

        commit = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=piko_directory,
            check=True,
            capture_output=True,
            text=True,
        )

    return PikoBuild(commit=commit.stdout.strip(), supported_versions=supported_versions)
