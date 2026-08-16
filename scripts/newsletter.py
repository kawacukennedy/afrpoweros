#!/usr/bin/env python3
"""Generate and send the AfrPowerOS Weekly newsletter via the Buttondown API.

Stdlib-only. Reads BUTTONDOWN_API_TOKEN from the environment or a .env file
in the repo root.

Usage:
  python3 scripts/newsletter.py --draft    # create a draft, do not send
  python3 scripts/newsletter.py --send     # create draft, then send immediately
  python3 scripts/newsletter.py --dry-run  # print the issue without calling the API
"""
import datetime
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SITE = ROOT / "site"
ISSUES_DIR = SITE / "newsletter"
API = "https://api.buttondown.com/v1"
ARCHIVE_URL = "https://buttondown.com/kawacu/archive/"


def load_token():
    env = os.environ.get("BUTTONDOWN_API_TOKEN")
    if env:
        return env.strip()
    env_file = ROOT / ".env"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            if line.startswith("BUTTONDOWN_API_TOKEN="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def api_request(method, path, payload=None, token=None):
    req = urllib.request.Request(API + path, method=method)
    req.add_header("Authorization", f"Token {token}")
    req.add_header("X-API-Version", "2026-04-01")
    req.add_header("Content-Type", "application/json")
    body = json.dumps(payload).encode("utf-8") if payload is not None else None
    try:
        with urllib.request.urlopen(req, data=body, timeout=30) as resp:
            raw = resp.read().decode("utf-8")
            return resp.status, json.loads(raw) if raw else {}
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        return exc.code, {"error": detail}


def next_issue_number():
    nums = []
    if ISSUES_DIR.exists():
        for p in ISSUES_DIR.glob("issue-*.html"):
            m = re.match(r"issue-(\d+)\.html", p.name)
            if m:
                nums.append(int(m.group(1)))
    return (max(nums) + 1) if nums else 1


def dataset_changes_since(days=7):
    changes = []
    try:
        since = (datetime.date.today() - datetime.timedelta(days=days)).isoformat()
        out = subprocess.run(
            ["git", "log", f"--since={since}", "--oneline", "--", "data/afrpoweros.json"],
            capture_output=True, text=True, cwd=ROOT,
        ).stdout
        for line in out.splitlines():
            changes.append(line.strip())
    except Exception:
        pass
    return changes


def build_issue():
    with open(DATA / "afrpoweros.json", encoding="utf-8") as fh:
        dataset = json.load(fh)
    countries = dataset["countries"]
    n = len(countries)

    statuses = {}
    verified = 0
    for rec in countries:
        s = rec.get("program_status", "None")
        statuses[s] = statuses.get(s, 0) + 1
        if rec.get("confidence") == "Verified":
            verified += 1

    label = {
        "Operating": "operating a commercial plant",
        "Under Construction": "under construction",
        "Announced": "announced",
        "Preparing": "preparing",
        "Exploring": "exploring",
        "None": "no active program",
    }

    status_lines = "\n".join(
        f"- **{count}** {label.get(s, s.lower())}" for s, count in sorted(statuses.items(), key=lambda kv: -kv[1])
    )

    changes = dataset_changes_since()
    change_block = "\n".join(f"- `{c}`" for c in changes[:8]) if changes else "None this week — records carried over from prior verification."

    body = f"""# AfrPowerOS Weekly

{datetime.date.today().isoformat()} · {n} countries tracked · every fact sourced

## This week in the dataset

{status_lines}

**Confidence:** {verified} of {n} records `Verified` from primary sources.

**Dataset changes (last 7 days):**
{change_block}

## Why this matters

Africa hosts under 2% of global data-center capacity, and ~600 million people in sub-Saharan Africa lack electricity. Power — not compute — is the binding constraint on the continent's AI and industrial future. AfrPowerOS tracks the civilian nuclear programs emerging to close that gap.

## Explore the data

- Live map: https://kawacukennedy.github.io/afrpoweros/
- Full dataset: https://github.com/kawacukennedy/afrpoweros/blob/main/data/afrpoweros.json
- Corrections welcome: https://github.com/kawacukennedy/afrpoweros/issues
- Archive: {ARCHIVE_URL}

*Every record carries a confidence label (Verified / Inference / Speculation / Unverified). Nothing is invented — if we can't source it, we mark it or omit it. No hype, no ads.*
"""
    subject = f"AfrPowerOS Weekly · {n} countries, {verified} verified · {datetime.date.today().isoformat()}"
    return subject, body


def write_archive_page(issue_num, subject, body):
    ISSUES_DIR.mkdir(parents=True, exist_ok=True)
    date = datetime.date.today().isoformat()
    html_body = body.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    html_body = html_body.replace("\n", "<br>")
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Issue {issue_num:03d} — AfrPowerOS Weekly</title>
  <link rel="stylesheet" href="../styles.css?v=__VER__">
</head>
<body>
  <header class="nav">
    <div class="nav-inner">
      <a class="brand" href="/"><span class="brand-dot"></span><span>AfrPowerOS</span></a>
      <nav class="nav-links">
        <a href="/#map">Map</a>
        <a href="/#table">Countries</a>
        <a href="../newsletter.html">Newsletter</a>
        <a class="nav-cta" href="https://github.com/kawacukennedy/afrpoweros">GitHub</a>
      </nav>
    </div>
  </header>
  <main>
    <article class="issue">
      <p class="eyebrow">Issue {issue_num:03d} · {date}</p>
      <h1>{subject.replace('<', '&lt;').replace('>', '&gt;')}</h1>
      <p>{html_body}</p>
      <form class="newsletter-form" action="https://buttondown.com/api/emails/embed-subscribe/kawacu" method="post" target="_blank">
        <input type="email" name="email" placeholder="you@example.com" required>
        <button type="submit" class="btn btn-primary">Subscribe free</button>
      </form>
    </article>
  </main>
  <footer class="footer">
    <p>AfrPowerOS · MIT code · CC BY 4.0 data</p>
    <p><a href="https://github.com/kawacukennedy/afrpoweros">github.com/kawacukennedy/afrpoweros</a> · <a href="https://github.com/kawacukennedy/afrpoweros/issues">Issues</a></p>
  </footer>
</body>
</html>
"""
    path = ISSUES_DIR / f"issue-{issue_num:03d}.html"
    path.write_text(page, encoding="utf-8")
    return path


def update_archive_index(issue_num, subject):
    index = SITE / "newsletter.html"
    if not index.exists():
        return
    text = index.read_text(encoding="utf-8")
    date = datetime.date.today().isoformat()
    li = f'<li><a href="newsletter/issue-{issue_num:03d}.html">Issue {issue_num:03d} — {subject}</a> <span class="newsletter-date">· {date}</span></li>'
    if f'issue-{issue_num:03d}.html' in text:
        return
    marker = '<ul class="archive-list">'
    if marker in text:
        text = text.replace(marker, marker + "\n        " + li, 1)
        index.write_text(text, encoding="utf-8")


def main():
    mode = "draft"
    if "--send" in sys.argv:
        mode = "send"
    elif "--dry-run" in sys.argv:
        mode = "dry-run"

    subject, body = build_issue()
    issue_num = next_issue_number()
    print(f"Issue {issue_num:03d}: {subject}")
    print("=" * 60)
    print(body)

    if mode == "dry-run":
        print("dry-run: no API call made")
        return 0

    token = load_token()
    if not token:
        print("FATAL: BUTTONDOWN_API_TOKEN not set (env or .env)", file=sys.stderr)
        return 1

    status, created = api_request(
        "POST", "/emails",
        {"subject": subject, "body": body, "status": "draft"},
        token=token,
    )
    if status not in (200, 201):
        print(f"FATAL: create email failed ({status}): {created}", file=sys.stderr)
        return 1
    email_id = created.get("id")
    url = created.get("absolute_url", "")
    print(f"draft created: {email_id} {url}")

    if mode == "send":
        st2, updated = api_request(
            "PATCH", f"/emails/{email_id}",
            {"status": "about_to_send"},
            token=token,
        )
        if st2 != 200:
            print(f"FATAL: send failed ({st2}): {updated}", file=sys.stderr)
            return 1
        print(f"SENT: {updated.get('absolute_url', url)}")

    page = write_archive_page(issue_num, subject, body)
    update_archive_index(issue_num, subject)
    print(f"archive page: {page}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
