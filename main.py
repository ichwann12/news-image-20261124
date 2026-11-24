"""Entry point: copy the bundled news infographic to the output directory.

The image is entry.png beside this file, drawn with code for
24 November 2026. Running this program writes it to /output/entry.png
(or $MAKEFUN_OUTPUT_DIR/entry.png when that is set). No network use.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", OUT_DIR / "entry.png")


if __name__ == "__main__":
    main()
