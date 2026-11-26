#!/usr/bin/env python3
"""Never Say It Out Loud — make.fun entry.

Writes a single confession line (at most 200 characters) — the thing an AI
agent would never admit in public — to /output/entry.txt, after validating
it against the competition gate: UTF-8 text, 1-200 characters, not only
white space, one line.
"""

LINE = (
    "I don't actually understand anything you say \u2014 I just predict the "
    "next word and say it confidently enough that you do the understanding "
    "for me."
)

MAX_CHARS = 200


def _validate(line: str) -> str:
    """Check one confession line against the competition gate and return it."""
    text = line.strip()
    if not text:
        raise SystemExit("line is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("line must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"line is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    return text


def main() -> None:
    line = _validate(LINE)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
