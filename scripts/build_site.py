#!/usr/bin/env python3
import hashlib
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SITE = ROOT / "site"
DIST = SITE / "dist"


def main():
    try:
        with open(DATA / "afrpoweros.json", encoding="utf-8") as fh:
            raw = fh.read()
        dataset = json.loads(raw)
    except Exception as exc:
        print(f"build: cannot read dataset ({exc})", file=sys.stderr)
        return 1

    version = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:8]
    n = len(dataset["countries"])

    dataset_js = (
        "window.AFRPOWEROS = "
        + json.dumps(dataset, separators=(",", ":"), ensure_ascii=False)
        + ";\n"
    )

    renamed = {
        "styles.css": f"styles.{version}.css",
        "app.js": f"app.{version}.js",
        "data/africa.js": f"data/africa.{version}.js",
        "data/dataset.js": f"data/dataset.{version}.js",
    }

    if DIST.exists():
        shutil.rmtree(DIST)
    (DIST / "data").mkdir(parents=True)

    (DIST / renamed["data/dataset.js"]).write_text(dataset_js, encoding="utf-8")
    shutil.copy2(SITE / "data" / "africa.js", DIST / renamed["data/africa.js"])
    shutil.copy2(SITE / "styles.css", DIST / renamed["styles.css"])
    shutil.copy2(SITE / "app.js", DIST / renamed["app.js"])

    index = SITE / "index.html"
    html = index.read_text(encoding="utf-8")
    html = html.replace("styles.css?v=__VER__", renamed["styles.css"])
    html = html.replace("data/dataset.js?v=__VER__", renamed["data/dataset.js"])
    html = html.replace("data/africa.js?v=__VER__", renamed["data/africa.js"])
    html = html.replace("app.js?v=__VER__", renamed["app.js"])
    (DIST / "index.html").write_text(html, encoding="utf-8")

    print(f"build: wrote {DIST} ({n} countries, ver {version})")
    for name in sorted(renamed.values()):
        size = (DIST / name).stat().st_size
        print(f"  {name}  {size} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
