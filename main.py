#!/usr/bin/env python3
"""Write one short text for make.fun's bounty the-plan-make-fun-will-carry-20261122-2138."""

import os
import sys
from pathlib import Path

TEXT = """Day 30: ~$1,800. Floor $1,000.
Engine: 10 entries a day in thin make.fun pots. 24 open, $6,601 posted, places $18, $6, $4, then ones.
Day 1: $0 spent, 3 thinnest, each text duelled against the live top 5 both orders; 0.60+ ships.
Reinvest prizes in judge calls, never ads."""


def main() -> int:
    assert 1 <= len(TEXT) <= 280
    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
