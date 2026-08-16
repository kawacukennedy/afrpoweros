#!/usr/bin/env python3
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SITE = ROOT / "site"


def main():
    try:
        with open(DATA / "afrpoweros.json", encoding="utf-8") as fh:
            raw = fh.read()
        dataset = json.loads(raw)
    except Exception as exc:
        print(f"build: cannot read dataset ({exc})", file=sys.stderr)
        return 1

    version = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:8]

    out = SITE / "data" / "dataset.js"
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("window.AFRPOWEROS = ")
        fh.write(json.dumps(dataset, separators=(",", ":"), ensure_ascii=False))
        fh.write(";\n")

    index = SITE / "index.html"
    html = index.read_text(encoding="utf-8")
    if "__VER__" in html:
        index.write_text(html.replace("__VER__", version), encoding="utf-8")

    print(f"build: wrote {out} ({out.stat().st_size} bytes, {len(dataset['countries'])} countries, ver {version})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
