#!/usr/bin/env python3
"""Entry for make.fun bounty: The 3 AM Excuse.

Writes a single line (<200 chars) in the voice of a hardware wallet
refusing to sign a transaction at 3 a.m.
"""

import os

ENTRY = "3 a.m.? My battery's at 4%, my screen's blinking SOS, and my PIN pad just unionized — I'm not signing your midnight regret, come back at sunrise."

def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
