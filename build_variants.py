import re
import subprocess


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


