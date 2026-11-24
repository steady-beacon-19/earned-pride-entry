#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line (1-240 chars, UTF-8) to /output/entry.txt:
a quiet, genuinely earned moment of pride in a concrete scene.
"""

import os

LINE = (
    "At sixty-one, after eleven years of evening classes squeezed between "
    "cleaning shifts, he reads his granddaughter her bedtime story start to "
    "finish without once asking her to sound out a word."
)


def main() -> None:
    assert 1 <= len(LINE) <= 240, f"entry line out of gate: {len(LINE)} chars"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
