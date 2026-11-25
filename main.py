#!/usr/bin/env python3
"""The 3 AM Excuse — one line in the voice of a hardware wallet that
refuses to sign a transaction at 3 AM. Stdlib only, no network, no I/O
beyond writing the entry."""

import os

ENTRY = (
    "It's 3 AM \u2014 my screen is dark, my buttons are on strike, "
    "and my battery's at 2%. Your 'urgent' trade can wait for "
    "sunrise like the rest of us."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
