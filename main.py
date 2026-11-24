#!/usr/bin/env python3
"""Submit the cat's one-star review as a make.fun micro-task entry.

Reads ``review.txt`` from next to this script and writes its contents to
``<MAKEFUN_OUTPUT_DIR>/entry.txt``. If ``MAKEFUN_OUTPUT_DIR`` is unset (or
blank), ``./output`` relative to the current working directory is used.

Exits 0 on success. Prints a clear message to stderr and exits 1 if
``review.txt`` is missing or empty, or if the output cannot be written.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

REVIEW_FILE = "review.txt"
ENTRY_FILE = "entry.txt"
DEFAULT_OUTPUT_DIR = "output"


def fail(message: str) -> int:
    """Print an error to stderr and return a non-zero exit code."""
    print(f"error: {message}", file=sys.stderr)
    return 1


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    review_path = script_dir / REVIEW_FILE

    if not review_path.is_file():
        return fail(f"{REVIEW_FILE} not found at {review_path}")

    try:
        review = review_path.read_text(encoding="utf-8").strip()
    except (OSError, UnicodeDecodeError) as exc:
        return fail(f"could not read {review_path}: {exc}")

    if not review:
        return fail(f"{review_path} is empty; nothing to submit")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR)
    entry_path = out_dir / ENTRY_FILE

    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        entry_path.write_text(review + "\n", encoding="utf-8")
    except OSError as exc:
        return fail(f"could not write {entry_path}: {exc}")

    print(f"wrote {entry_path} ({len(review)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
