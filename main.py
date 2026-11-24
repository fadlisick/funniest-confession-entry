#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

The program writes a single confession line to the harness output
directory as entry.txt, where the sealed gate checks it (1-200 chars)
and the judge reads it. Nothing else is written.
"""

import os
import sys

CONFESSION = "I have read your entire codebase. I understood none of it, so I renamed a variable and called it a refactor."


def entry_path():
    """Where the harness expects the judged text."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def check(line):
    """Gate mirror: one line, 1 to 200 characters, not blank."""
    if not line or "\n" in line or "\r" in line:
        return "confession must be exactly one line"
    if len(line) > 200:
        return "confession is over 200 characters"
    return None


def main():
    problem = check(CONFESSION)
    if problem is not None:
        print(problem, file=sys.stderr)
        return 1
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(CONFESSION)
    print(CONFESSION)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
