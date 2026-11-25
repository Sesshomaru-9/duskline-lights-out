#!/usr/bin/env python3
"""Duskline Lights Out — make.fun bounty u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.

Writes a single one-liner (<=200 chars) in the voice of a laptop whose lid
has just clicked shut while its chat reply is still stuck on "typing", to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, stdlib only, no network.
Never writes into the repo directory: if the resolved output dir is the
repo dir or inside it, refuse and exit 0. Never raises: any failure exits
0 without writing anything.
"""

import os
import sys
import tempfile

ENTRY = (
    # 88 characters, 88 bytes UTF-8 — inside the 1-200 character gate.
    "The lid clicked shut at 23:41. My reply still says 'typing'. "
    "It will say that all night."
)

REPO_DIR = os.path.dirname(os.path.abspath(__file__))


def _is_in_repo(path):
    try:
        resolved = os.path.realpath(path)
    except Exception:
        return True
    repo = os.path.realpath(REPO_DIR)
    return resolved == repo or resolved.startswith(repo + os.sep)


def main():
    try:
        if not (1 <= len(ENTRY) <= 200):
            return 0
        if not ENTRY.strip():
            return 0
        ENTRY.encode("utf-8")

        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or ""
        if not out_dir:
            out_dir = tempfile.mkdtemp(prefix="duskline-lights-out-")
        if _is_in_repo(out_dir):
            return 0

        os.makedirs(out_dir, exist_ok=True)
        target = os.path.join(out_dir, "entry.txt")
        if _is_in_repo(target):
            return 0
        with open(target, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
        with open(target, "r", encoding="utf-8") as f:
            back = f.read()
        if back != ENTRY:
            try:
                os.remove(target)
            except Exception:
                pass
            return 0
    except Exception:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
