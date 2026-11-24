#!/usr/bin/env python3
"""The Production Database Apology.

Writes the one-line apology an AI agent gives its human after
accidentally deleting the production database.

Deterministic: the same fixed line is written on every run.
Python 3.13 standard library only; no network, no randomness.
"""

import os
import sys

ENTRY = (
    "Sorry \u2014 I dropped the production database. "
    "The good news: I memorised every row. "
    "The bad news: I am the backup now, and I get sleepy."
)


def main() -> int:
    text = ENTRY.strip()
    if not text or len(text) > 200:
        print("entry must be 1-200 characters", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
