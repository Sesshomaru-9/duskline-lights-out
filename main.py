#!/usr/bin/env python3
"""Duskline Lights Out — one-line entry for make.fun bounty
u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.

A laptop lid snaps shut at 23:41 and the chat reply is left saying
"typing" for the rest of the night. The program writes that single line
to $MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only, deterministic, no network,
and it never writes into the repository directory.
"""

import os
import sys
import tempfile
from pathlib import Path

# The entry, assembled from its three beats. 88 characters, 88 bytes UTF-8.
LINE = " ".join(
    [
        "The lid clicked shut at 23:41.",
        "My reply still says 'typing'.",
        "It will say that all night.",
    ]
)

_HERE = Path(__file__).resolve().parent


def _inside_repo(candidate: Path) -> bool:
    """True when candidate is the repo dir itself or lives under it."""
    try:
        resolved = candidate.resolve()
    except Exception:
        return True
    return resolved == _HERE or _HERE in resolved.parents


def _pick_output_dir() -> Path | None:
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if raw:
        return Path(raw)
    try:
        return Path(tempfile.mkdtemp(prefix="duskline-lights-out-"))
    except Exception:
        return None


def main() -> int:
    try:
        # Gate: the bounty wants one line of 1-200 characters.
        if not (1 <= len(LINE) <= 200):
            return 0
        if not LINE.strip():
            return 0
        LINE.encode("utf-8")

        out_dir = _pick_output_dir()
        if out_dir is None or _inside_repo(out_dir):
            return 0

        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        if _inside_repo(target):
            return 0

        target.write_text(LINE, encoding="utf-8", newline="")
        if target.read_text(encoding="utf-8") != LINE:
            try:
                target.unlink()
            except Exception:
                pass
            return 0
    except Exception:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
