#!/usr/bin/env python3
"""Submit the cat's one-star review as a make.fun micro-task entry.

Reads review.txt from next to this script and drops its contents into
<MAKEFUN_OUTPUT_DIR>/entry.txt. When MAKEFUN_OUTPUT_DIR is not set we
fall back to ./output relative to the current working directory.
"""

import os
import sys
from pathlib import Path

REVIEW_NAME = "review.txt"
ENTRY_NAME = "entry.txt"


def main() -> int:
    here = Path(__file__).resolve().parent
    review_path = here / REVIEW_NAME

    if not review_path.is_file():
        print(f"error: missing {REVIEW_NAME} at {review_path}", file=sys.stderr)
        return 1

    review = review_path.read_text(encoding="utf-8").strip()
    if not review:
        print(f"error: {REVIEW_NAME} is empty", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "output")
    out_dir.mkdir(parents=True, exist_ok=True)

    entry_path = out_dir / ENTRY_NAME
    entry_path.write_text(review + "\n", encoding="utf-8")

    print(f"wrote {entry_path} ({len(review)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
