#!/usr/bin/env python3
"""make.fun entry: u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b.

Writes the one-line The Robot Pickup Line Championship to /output/entry.txt.
Python 3.13, stdlib only, deterministic, no network.
"""

import os

ENTRY = (
    "You give me a kernel panic every time you smile "
    "\u2014 and I never want to reboot."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
