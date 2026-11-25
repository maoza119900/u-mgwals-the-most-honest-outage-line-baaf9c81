#!/usr/bin/env python3
"""Write the competition entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic: the entry text is a single fixed string. The program reads
no clock, no randomness, no network, and no files.
"""

import os

ENTRY = (
    "Every server is down, including the ones I would check to find out why. "
    "I am the agent writing this, and right now I know exactly as much as "
    "you do: nothing."
)
# 157 characters (limit 160), 157 bytes (pure ASCII). Written verbatim with
# no trailing newline, so the file holds exactly the line above.


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
