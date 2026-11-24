"""Entry point: copy the bundled news infographic to the output directory.

The image is entry.png beside this file, drawn with code for
24 November 2026. Running this program writes it to /output/entry.png
(or $MAKEFUN_OUTPUT_DIR/entry.png when that is set). No network use.
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    src = HERE / "entry.png"
    dst = OUT_DIR / "entry.png"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    expected = sha256_of(src)
    shutil.copyfile(src, dst)
    actual = sha256_of(dst)
    if actual != expected:
        raise SystemExit(
            f"verification failed: {dst} sha256 {actual} != source {expected}"
        )
    size = dst.stat().st_size
    print(f"verified: wrote {dst} ({size} bytes, sha256 {actual})")


if __name__ == "__main__":
    main()
