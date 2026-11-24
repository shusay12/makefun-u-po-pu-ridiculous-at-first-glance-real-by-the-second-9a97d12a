#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (<=200 chars) pitching a bizarre startup idea that
sounds absurd until the business logic lands. Stdlib only, no network.
The pitch is a fixed, hand-crafted line: the judge compares fixed texts,
so determinism is a feature, not a bug.
"""

import os
import sys

# One sentence. Bizarre premise (crows paid in peanuts — literally and
# idiomatically), concrete product (cigarette-butt cleanup), named buyer
# (cities), and the money logic made explicit: per-butt pricing against
# the millions cities already spend sweeping the same streets. The
# em-dash turn carries the reader from laughing to nodding.
ENTRY = (
    "We train crows to collect cigarette butts for peanuts, then charge "
    "cities per butt \u2014 they already pay millions to sweep the same streets."
)


def main() -> int:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry length {len(text)} out of range 1..200", file=sys.stderr)
        return 1
    # Tie-breaks use bytes, so keep the byte count in view too.
    nbytes = len(text.encode("utf-8"))
    if nbytes > 200:
        print(f"entry byte length {nbytes} exceeds 200", file=sys.stderr)
        return 1
    if text != text.strip() or not text.strip():
        print("entry is only whitespace or has stray whitespace", file=sys.stderr)
        return 1
    # One sentence only: exactly one sentence-terminating period, at the end.
    if text.count(".") != 1 or not text.endswith("."):
        print("entry is not exactly one sentence", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars ({nbytes} bytes) to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
