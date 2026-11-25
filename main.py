#!/usr/bin/env python3
"""One Star for Monday.

Writes a one-star review of Monday as if it were a restaurant, at
most 25 words and 1-180 characters, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Python standard library only, no network calls,
always writes the same bytes. The gate is validated before writing.
"""

import os
import sys

LINE = (
    "One star. Monday served cold coffee, a 9 AM meeting, and a Wi-Fi "
    "outage as the main course. Left hungry, still billed."
)


def main():
    if not 1 <= len(LINE) <= 180:
        sys.exit(f"gate failed: line is {len(LINE)} chars, need 1-180")
    if len(LINE.split()) > 25:
        sys.exit(f"gate failed: line is {len(LINE.split())} words, need <= 25")
    if not LINE.strip() or "\n" in LINE:
        sys.exit("gate failed: line must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
