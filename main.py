#!/usr/bin/env python3
"""Emit the sharpened one-star review of Monday (batch 5, v3).

The program prints nothing and takes no input: it just drops a single
review line into entry.txt under the directory named by
MAKEFUN_OUTPUT_DIR, falling back to /output. The line is a diner's
complaint about Monday treated as a restaurant — a waiter, a dish that
went wrong, and a bill that showed up too soon.

Only the standard library is used, nothing is fetched from the network,
and the bytes written are identical on every run. Before writing, the
line is measured against the competition gate: one line, 1-180
characters, no more than 25 words, and not blank.
"""

from pathlib import Path
import os
import sys

REVIEW = (
    "One star. Monday's waiter brought cold coffee, "
    "a meeting I never ordered, and the check before "
    "the food arrived."
)


def validate(text):
    """Return an error string when the line breaks the gate, else None."""
    if not text or not text.strip():
        return "review is empty"
    if "\n" in text or "\r" in text:
        return "review must fit on one line"
    if len(text) > 180:
        return f"review is {len(text)} characters, over the 180 limit"
    words = text.split()
    if len(words) > 25:
        return f"review is {len(words)} words, over the 25 limit"
    return None


def run():
    problem = validate(REVIEW)
    if problem is not None:
        print(f"gate: {problem}", file=sys.stderr)
        return 1
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "entry.txt").write_text(REVIEW, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
