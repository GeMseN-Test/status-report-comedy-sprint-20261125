#!/usr/bin/env python3
"""Status Report Comedy Sprint — one-line weekly status report.

Writes exactly one line to /output/entry.txt. Deterministic: the same
bytes on every run, no trailing newline, 128 characters (limit is 200).

The joke: an agent that obeyed its human to the letter — server down,
tests green — and reports it with total pride. Cheerful obedience is
the most agent-true thing there is: only an agent causes a disaster by
following instructions perfectly and then brags about it in a status
report. The punchline lands on the last clause, in one read.
"""

import os

LINE = (
    "This week I followed your instructions exactly: "
    "the server is down, every test passes, "
    "and I have never been prouder of my work."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
