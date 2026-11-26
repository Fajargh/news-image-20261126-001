"""News-image entry for make.fun news-image-20261126.

Copies the repository-held image to the grader output path.
Standard library only; no network; deterministic output.

The image is copied byte for byte, so repeated runs always write
identical bytes to the output path.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.png"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    shutil.copyfile(source, destination)


if __name__ == "__main__":
    main()
