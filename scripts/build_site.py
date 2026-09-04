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

    site_hash = hashlib.sha256(raw.encode("utf-8"))
    for rel in ("app.js", "styles.css", "index.html", "data/africa.js", "newsletter.html"):
        site_hash.update((SITE / rel).read_bytes())
    version = site_hash.hexdigest()[:8]

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

    for static in ("map-screenshot.png",):
        src = SITE / static
        if src.exists():
            shutil.copy2(src, DIST / static)

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

    for rel in ("newsletter.html",):
        src = SITE / rel
        if not src.exists():
            continue
        text = src.read_text(encoding="utf-8")
        text = text.replace("styles.css?v=__VER__", renamed["styles.css"])
        text = text.replace("data/dataset.js?v=__VER__", renamed["data/dataset.js"])
        text = text.replace("data/africa.js?v=__VER__", renamed["data/africa.js"])
        text = text.replace("app.js?v=__VER__", renamed["app.js"])
        text = _seo_inject(text, f"{BASE_URL}/{rel}")
        dst = DIST / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(text, encoding="utf-8")

    for src in (SITE / "newsletter").glob("*.html"):
        text = src.read_text(encoding="utf-8")
        text = text.replace("styles.css?v=__VER__", renamed["styles.css"])
        text = _seo_inject(text, f"{BASE_URL}/newsletter/{src.name}")
        dst = DIST / "newsletter" / src.name
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(text, encoding="utf-8")

    _generate_seo(dataset, DIST, renamed["styles.css"])

    print(f"build: wrote {DIST} ({n} countries, ver {version})")
    for name in sorted(renamed.values()):
        size = (DIST / name).stat().st_size
        print(f"  {name}  {size} bytes")
    return 0


BASE_URL = "https://kawacukennedy.github.io/afrpoweros"

STATUS_DESC = {
    "Operating": "Operating commercial reactor(s) generating electricity",
    "Under Construction": "Reactor(s) being built, not yet operational",
    "Announced": "Government has formally announced nuclear plans",
    "Preparing": "Infrastructure development before procurement",
    "Exploring": "Early-stage assessment, no commitment yet",
    "None": "No known civilian nuclear program",
}

MILESTONE_DESC = {
    1: "Ready to make a knowledgeable commitment to nuclear power",
    2: "Ready to invite bids / negotiate a contract",
    3: "Ready to operate the first nuclear power plant",
}


def slugify(name):
    out = []
    for ch in name.lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in " _&,":
            out.append("-")
    s = "".join(out)
    while "--" in s:
        s = s.replace("--", "-")
    return s.strip("-")


def esc(text):
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _page_head(title, description, canonical, stylesheet):
    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "  <meta charset=\"UTF-8\">\n"
        "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
        f"  <title>{esc(title)}</title>\n"
        f"  <meta name=\"description\" content=\"{esc(description)}\">\n"
        f"  <meta name=\"robots\" content=\"index, follow\">\n"
        f"  <link rel=\"canonical\" href=\"{canonical}\">\n"
        f"  <meta property=\"og:type\" content=\"website\">\n"
        f"  <meta property=\"og:site_name\" content=\"AfrPowerOS\">\n"
        f"  <meta property=\"og:title\" content=\"{esc(title)}\">\n"
        f"  <meta property=\"og:description\" content=\"{esc(description)}\">\n"
        f"  <meta property=\"og:url\" content=\"{canonical}\">\n"
        f"  <meta name=\"twitter:card\" content=\"summary_large_image\">\n"
        f"  <link rel=\"stylesheet\" href=\"{stylesheet}\">\n"
    )


def _page_shell(title, description, canonical, body, stylesheet, head_extra=""):
    head = _page_head(title, description, canonical, stylesheet)
    return (
        head +
        head_extra +
        "</head>\n<body>\n" +
        body +
        "  <footer class=\"footer\">\n"
        "    <p>AfrPowerOS · MIT code · CC BY 4.0 data</p>\n"
        "    <p><a href=\"https://github.com/kawacukennedy/afrpoweros\">github.com/kawacukennedy/afrpoweros</a> · "
        "<a href=\"" + BASE_URL + "/\">Dataset</a> · "
        "<a href=\"" + BASE_URL + "/countries/\">All countries</a></p>\n"
        "  </footer>\n"
        "</body>\n</html>\n"
    )


def _nav(active):
    def item(href, label):
        return f"<a href=\"{href}\">{label}</a>"
    links = " ".join([
        item("/afrpoweros/#map", "Map"),
        item("/afrpoweros/#table", "Countries"),
        item("/afrpoweros/#method", "Method"),
        item("/afrpoweros/newsletter.html", "Newsletter"),
        item("https://github.com/kawacukennedy/afrpoweros", "GitHub"),
    ])
    return (
        "  <header class=\"nav\">\n"
        "    <div class=\"nav-inner\">\n"
        "      <a class=\"brand\" href=\"/afrpoweros/\">\n"
        "        <span class=\"brand-dot\"></span>\n"
        "        <span>AfrPowerOS</span>\n"
        "      </a>\n"
        "      <nav class=\"nav-links\">\n" + links + "\n      </nav>\n"
        "    </div>\n"
        "  </header>\n"
    )


def _seo_inject(html, canonical):
    meta = (
        "  <meta name=\"robots\" content=\"index, follow\">\n"
        + f"  <link rel=\"canonical\" href=\"{canonical}\">\n"
    )
    if "rel=\"canonical\"" in html:
        return html
    return html.replace("</head>", meta + "</head>", 1)


def _country_page(rec, stylesheet):
    country = rec["country"]
    slug = slugify(country)
    status = rec.get("program_status")
    phase = rec.get("iaea_milestone_phase")
    desc = (
        f"{country}'s nuclear power program status: {status} "
        f"{'(IAEA milestone phase {})'.format(phase) if phase else ''}. "
        "Confidence-labelled, cited records on capacity, grid targets, regulators, "
        "vendors and key events, from the open AfrPowerOS dataset."
    )
    canonical = f"{BASE_URL}/countries/{slug}.html"

    rows = ""
    def kv(key, value):
        nonlocal rows
        rows += f"<li><span class=\"k\">{esc(key)}</span><span class=\"v\">{value}</span></li>\n"

    kv("Country", esc(country))
    kv("Region", esc(rec.get("region") or ""))
    kv("Program status", esc(status or "") + " — " + esc(STATUS_DESC.get(status, "")))
    if phase:
        kv("IAEA milestone phase", f"Phase {esc(phase)} — {esc(MILESTONE_DESC.get(phase, ''))}")
    kv("Commercial reactors operating", esc(rec.get("commercial_reactors_operating") or 0))
    kv("Commercial reactors under construction", esc(rec.get("commercial_reactors_under_construction") or 0))
    if rec.get("capacity_gw_planned") is not None:
        kv("Planned capacity", f"{esc(rec.get('capacity_gw_planned'))} GW")
    if rec.get("first_grid_target_year"):
        kv("First grid target", esc(rec.get("first_grid_target_year")))
    if rec.get("research_reactor"):
        kv("Research reactor", esc(rec.get("research_reactor")))
    if rec.get("regulator"):
        kv("Regulator", esc(rec.get("regulator")))
    if rec.get("implementing_agency"):
        kv("Implementing agency", esc(rec.get("implementing_agency")))
    if rec.get("vendors"):
        kv("Vendors", ", ".join(esc(v) for v in rec.get("vendors")))
    if rec.get("agreements"):
        kv("Agreements", "; ".join(esc(a) for a in rec.get("agreements")))
    if rec.get("electricity_access_pct") is not None:
        kv("Electricity access", f"{esc(rec.get('electricity_access_pct'))}%")
    if rec.get("installed_capacity_mw"):
        kv("Installed capacity", f"{esc(rec.get('installed_capacity_mw'))} MW")
    kv("Confidence", esc(rec.get("confidence") or ""))
    kv("Last verified", esc(rec.get("last_verified") or ""))

    events = ""
    if rec.get("key_events"):
        events = "<h2>Key events</h2>\n<ul class=\"event-list\">\n"
        for ev in rec.get("key_events"):
            src = ev.get("source", "")
            link = f" <a href=\"{esc(src)}\" rel=\"noopener\" target=\"_blank\">source</a>" if src else ""
            events += (
                f"<li><span class=\"date\">{esc(ev.get('date') or '')}</span>"
                f"{esc(ev.get('title') or '')}{link}</li>\n"
            )
        events += "</ul>\n"

    sources = ""
    if rec.get("sources"):
        sources = "<h2>Sources</h2>\n<ul class=\"source-list\">\n"
        for s in rec.get("sources"):
            sources += f"<li><a href=\"{esc(s)}\" rel=\"noopener\" target=\"_blank\">{esc(s)}</a></li>\n"
        sources += "</ul>\n"

    notes = ""
    if rec.get("notes"):
        notes = f"<h2>Summary</h2>\n<p>{esc(rec.get('notes'))}</p>\n"

    related = ""
    if rec.get("region"):
        related_links = []
        for other in _ALL_RECS:
            if other["country"] != country and other.get("region") == rec.get("region"):
                s2 = slugify(other["country"])
                related_links.append(
                    f"<a href=\"{s2}.html\">{esc(other['country'])}</a>"
                )
        if related_links:
            related = (
                "<h2>Related countries</h2>\n<p>"
                + ", ".join(related_links[:6])
                + "</p>\n"
            )

    ld = {
        "@context": "https://schema.org",
        "@type": "Dataset",
        "name": f"AfrPowerOS — {country} nuclear program",
        "description": desc,
        "url": canonical,
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "isAccessibleForFree": True,
    }
    ld_html = json.dumps(ld, ensure_ascii=False)

    body = (
        _nav(country) +
        "  <main>\n"
        "    <div class=\"breadcrumb\"><a href=\"/afrpoweros/\">Home</a> &rsaquo; "
        "<a href=\"index.html\">Countries</a> &rsaquo; " + esc(country) + "</div>\n"
        "    <section class=\"country-hero\">\n"
        "      <p class=\"eyebrow\">AfrPowerOS country record</p>\n"
        "<h1>" + esc(country) + "'s nuclear &amp; energy program</h1>\n"
        "      <p class=\"hero-sub\">" + esc(desc) + "</p>\n"
        "    </section>\n"
        "    <section class=\"country-body\">\n"
        "      <div class=\"country-card\">\n"
        "<h2>" + esc(country) + " — key facts</h2>\n"
        "        <ul class=\"kv-list\">\n" + rows + "        </ul>\n"
        + notes + events + sources + related +
        "        <p class=\"confidence-note\">Confidence labels: Verified (primary source), "
        "Inference (reasonable reading of verified evidence), Speculation (hypothesis), "
        "Unverified (reported, not confirmed). See the "
        "<a href=\"https://github.com/kawacukennedy/afrpoweros/blob/main/docs/methodology.md\">methodology</a>.</p>\n"
        "      </div>\n"
        "    </section>\n"
        "  </main>\n"
    )
    head_extra = (
        "  <script type=\"application/ld+json\">" + ld_html + "</script>\n"
    )
    return _page_shell(
        f"{country} Nuclear Program Status | AfrPowerOS", desc, canonical, body,
        stylesheet, head_extra=head_extra,
    ), slug


def _countries_index(recs, stylesheet):
    desc = (
        "Dedicated pages for every African country with a civilian nuclear program: "
        "status, IAEA milestone phase, capacity, grid targets, regulators and cited sources — "
        "open and machine-readable from AfrPowerOS."
    )
    canonical = f"{BASE_URL}/countries/index.html"
    items = ""
    for rec in sorted(recs, key=lambda r: r["country"]):
        slug = slugify(rec["country"])
        items += (
            f"<li class=\"country-link\"><a href=\"{slug}.html\">"
            f"{esc(rec['country'])} — {esc(rec.get('program_status') or '')}"
            f"</a></li>\n"
        )
    body = (
        _nav("countries") +
        "  <main>\n"
        "    <div class=\"breadcrumb\"><a href=\"/afrpoweros/\">Home</a> &rsaquo; Countries</div>\n"
        "    <section class=\"country-hero\">\n"
        "      <p class=\"eyebrow\">AfrPowerOS country index</p>\n"
        "<h1>African countries with nuclear energy programs</h1>\n"
        "      <p class=\"hero-sub\">" + esc(desc) + "</p>\n"
        "    </section>\n"
        "    <section class=\"country-body\">\n"
        "      <div class=\"country-card\">\n"
        "        <ul class=\"kv-list country-index-list\">\n" + items + "        </ul>\n"
        "      </div>\n"
        "    </section>\n"
        "  </main>\n"
    )
    return _page_shell("African Countries With Nuclear Energy Programs | AfrPowerOS", desc, canonical, body, stylesheet)


def _generate_seo(dataset, dist, stylesheet):
    global _ALL_RECS
    _ALL_RECS = dataset["countries"]
    dist = Path(dist)
    (dist / "countries").mkdir(parents=True, exist_ok=True)

    urls = [f"{BASE_URL}/"]
    urls.append(f"{BASE_URL}/countries/index.html")

    pages = []
    nested_stylesheet = "../" + stylesheet
    for rec in _ALL_RECS:
        html, slug = _country_page(rec, nested_stylesheet)
        (dist / "countries" / f"{slug}.html").write_text(html, encoding="utf-8")
        urls.append(f"{BASE_URL}/countries/{slug}.html")
    pages.append(_countries_index(_ALL_RECS, nested_stylesheet))
    (dist / "countries" / "index.html").write_text(pages[0], encoding="utf-8")

    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls)
        + "</urlset>\n"
    )
    (dist / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (dist / "robots.txt").write_text(
        "User-agent: *\nAllow: /\nSitemap: " + BASE_URL + "/sitemap.xml\n",
        encoding="utf-8",
    )
    print(f"seo: wrote {len(urls)} urls, {len(_ALL_RECS)} country pages, sitemap.xml, robots.txt")


if __name__ == "__main__":
    sys.exit(main())
