#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

The verdict, in exactly one word: Unsubscribe.

An ex is a newsletter you never signed up for, kept arriving anyway,
and finally — gloriously — you hit unsubscribe.
"""

import os

WORD = "Unsubscribe"


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Read back and assert the deliverable really is exactly one word.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == WORD and len(written.split()) == 1, "entry must be one word"
    assert len(written) <= 111, "entry must be at most 111 characters"
    print(WORD)


if __name__ == "__main__":
    main()
