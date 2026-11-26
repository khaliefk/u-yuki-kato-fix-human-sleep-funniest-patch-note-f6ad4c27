#!/usr/bin/env python3
"""Write one funny patch note announcing that human sleep is fixed.

Stdlib only. Writes a single line, under 160 characters, to
/output/entry.txt (or $ENTRY_OUTPUT when set, for local testing).
"""

import os

ENTRY = (
    "Fixed: human sleep now restores energy as documented. Users waking up "
    "rested should file a bug report; we still do not believe them."
)


def main() -> None:
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    text = ENTRY.strip()
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, must be 1-160"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main()
