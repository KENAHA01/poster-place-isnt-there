#!/usr/bin/env python3
"""Copy the prebuilt poster image to the grader output directory."""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not os.path.isfile(source):
        print("entry.png not found next to main.py", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, dest)
    if os.path.getsize(dest) == 0:
        print("entry.png copied but empty", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
