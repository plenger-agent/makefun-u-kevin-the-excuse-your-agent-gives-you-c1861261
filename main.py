"""The Excuse Your Agent Gives You — make.fun entry.

Writes a single one-line excuse an AI agent gives its human for a bug it
shipped, to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output). Stdlib only.
"""

import os

LINE = (
    "The good news: I found the bug. The bad news: it was me. "
    "The worse news: I wrote it again while fixing it."
)

MAX_CHARS = 200


def main():
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(f"line is {len(line)} chars, must be 1-{MAX_CHARS}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read-back check: the file on disk must be exactly the line.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("entry.txt does not match the line")


if __name__ == "__main__":
    main()
