#!/usr/bin/env python3
"""One Star for Monday — a one-star review of Monday, written as though
Monday were a restaurant.

The program writes exactly one line of plain text to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt). The line is a
diner's complaint: the weekend was ordered, Monday got served instead, and
the bill covers waking up. It stays inside the bounty gate (1-180 chars,
one line, non-whitespace UTF-8) and inside the task limit (at most 25
words). No input, no network, no randomness, no clock: the same line
every run.
"""

import hashlib
import os
import sys

REVIEW = (
    "One star. Ordered the weekend, got served Monday: cold coffee, "
    "a 9am meeting, and the waiter billed me for waking up."
)

MAX_CHARS = 180
MAX_WORDS = 25


def count_words(text):
    """Words are whitespace-separated tokens."""
    return len(text.split())


def passes_gate(text):
    """Mirror of the sealed gate, plus the task's 25-word limit."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= MAX_CHARS):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if count_words(text) > MAX_WORDS:
        return False
    return True


def main():
    if not passes_gate(REVIEW):
        print("gate check failed for the review line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = REVIEW.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    with open(path, "rb") as handle:
        on_disk = handle.read()
    if on_disk != data:
        print("round-trip mismatch: disk bytes differ", file=sys.stderr)
        return 1
    back = on_disk.decode("utf-8")
    if back != REVIEW or not passes_gate(back):
        print("gate check failed on the file as written", file=sys.stderr)
        return 1
    if back.endswith("\n"):
        print("trailing newline found", file=sys.stderr)
        return 1
    if back.count("\n") != 0 or len(back.splitlines()) != 1:
        print("file is not exactly one line", file=sys.stderr)
        return 1
    print(back)
    print("chars=%d words=%d" % (len(back), count_words(back)))
    print("sha256=%s" % hashlib.sha256(on_disk).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
