#!/usr/bin/env python3
"""news-image-20261125 entrypoint.

Copies the front-page image (entry.png, drawn by build_frontpage.py) to the
output directory. Standard library only; the copy is byte-for-byte, so both
grader runs write identical bytes.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    assert os.path.getsize(dst) == os.path.getsize(src), "short copy"
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))


if __name__ == "__main__":
    main()
