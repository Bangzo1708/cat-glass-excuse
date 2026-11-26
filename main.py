#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — make.fun entry.

Writes the single sentence a house cat would say in its own defence
after sweeping a glass off the table, to /output/entry.txt.

The text is fixed and deterministic: the program always writes exactly
the same sentence, so both grading runs produce identical output.
"""

import os
import stat

ENTRY_TEXT = (
    "That glass had been squatting on my sunspot for three days, "
    "so I served it an eviction notice."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text, not only whitespace.
    text = ENTRY_TEXT.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text == ENTRY_TEXT, "entry must be a single unchanged sentence"

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write atomically via a temp file in the same directory, so a reader
    # never sees a half-written entry if the run is interrupted mid-write.
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(tmp_path, 0o644)
    os.replace(tmp_path, OUTPUT_PATH)


if __name__ == "__main__":
    main()
