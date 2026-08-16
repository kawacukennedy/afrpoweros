#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SITE = ROOT / "site"


def main():
    try:
        with open(DATA / "afrpoweros.json", encoding="utf-8") as fh:
            dataset = json.load(fh)
    except Exception as exc:
        print(f"build: cannot read dataset ({exc})", file=sys.stderr)
        return 1

    out = SITE / "data" / "dataset.js"
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("window.AFRPOWEROS = ")
        fh.write(json.dumps(dataset, separators=(",", ":"), ensure_ascii=False))
        fh.write(";\n")

    print(f"build: wrote {out} ({out.stat().st_size} bytes, {len(dataset['countries'])} countries)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
