#!/usr/bin/env python3
import csv
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

REGIONS = {"East Africa", "West Africa", "North Africa", "Central Africa", "Southern Africa"}
STATUSES = {"Operating", "Under Construction", "Announced", "Preparing", "Exploring", "None"}
CONFIDENCES = {"Verified", "Inference", "Speculation", "Unverified"}
REQUIRED_FIELDS = [
    "country", "region", "program_status", "iaea_milestone_phase",
    "commercial_reactors_operating", "commercial_reactors_under_construction",
    "capacity_gw_planned", "first_grid_target_year", "research_reactor",
    "regulator", "implementing_agency", "vendors", "agreements",
    "electricity_access_pct", "installed_capacity_mw", "notes",
    "key_events", "sources", "confidence", "last_verified",
]
CSV_HEADER = [
    "country", "region", "program_status", "iaea_milestone_phase",
    "capacity_gw_planned", "first_grid_target_year", "regulator",
    "implementing_agency", "research_reactor", "confidence", "last_verified",
]
CSV_MATCH_FIELDS = ["program_status", "capacity_gw_planned", "first_grid_target_year", "regulator", "implementing_agency", "confidence", "last_verified"]
DATE_RE = re.compile(r"^\d{4}(-\d{2})?$")

errors = []
records = 0


def fail(msg):
    errors.append(msg)


def load_json(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except Exception as exc:
        fail(f"{path.name}: cannot parse JSON ({exc})")
        return None


def valid_date(s):
    if not isinstance(s, str):
        return False
    try:
        datetime.date.fromisoformat(s)
        return True
    except ValueError:
        return False


def check_optional_number(value, field, country, lo=None, hi=None):
    if value is None:
        return
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        fail(f"{country}: {field} must be a number or null")
        return
    if lo is not None and value < lo:
        fail(f"{country}: {field} below minimum {lo}")
    if hi is not None and value > hi:
        fail(f"{country}: {field} above maximum {hi}")


def check_optional_int(value, field, country, lo=None, hi=None):
    if value is None:
        return
    if not isinstance(value, int) or isinstance(value, bool):
        fail(f"{country}: {field} must be an integer or null")
        return
    if lo is not None and value < lo:
        fail(f"{country}: {field} below minimum {lo}")
    if hi is not None and value > hi:
        fail(f"{country}: {field} above maximum {hi}")


def check_string(value, field, country):
    if not isinstance(value, str) or not value.strip():
        fail(f"{country}: {field} must be a non-empty string")


def check_string_list(value, field, country, min_items=0):
    if not isinstance(value, list):
        fail(f"{country}: {field} must be a list")
        return
    if min_items and len(value) < min_items:
        fail(f"{country}: {field} must have at least {min_items} item(s)")
    for item in value:
        if not isinstance(item, str):
            fail(f"{country}: {field} entries must be strings")


def main():
    global records
    schema = load_json(DATA / "schema.json")
    dataset = load_json(DATA / "afrpoweros.json")

    if schema is not None:
        if not isinstance(schema, dict):
            fail("schema.json: must be an object")
        elif "definitions" not in schema:
            fail("schema.json: missing 'definitions'")

    if dataset is None:
        print_errors()
        return 1

    if not isinstance(dataset, dict) or "countries" not in dataset:
        fail("afrpoweros.json: missing 'countries' key")
        print_errors()
        return 1

    countries = dataset["countries"]
    if not isinstance(countries, list) or not countries:
        fail("afrpoweros.json: 'countries' must be a non-empty list")
        print_errors()
        return 1

    seen = {}
    for record in countries:
        records += 1
        if not isinstance(record, dict):
            fail(f"record {records}: must be an object")
            continue
        country = record.get("country", "<unknown>")
        if not isinstance(country, str) or not country.strip():
            fail(f"record {records}: missing or invalid 'country'")
            country = "<unknown>"
        else:
            key = country.lower()
            if key in seen:
                fail(f"{country}: duplicate country record (also at index {seen[key]})")
            seen[key] = records - 1

        for field in REQUIRED_FIELDS:
            if field not in record:
                fail(f"{country}: missing required field '{field}'")

        region = record.get("region")
        if region not in REGIONS:
            fail(f"{country}: invalid region '{region}'")
        status = record.get("program_status")
        if status not in STATUSES:
            fail(f"{country}: invalid program_status '{status}'")
        conf = record.get("confidence")
        if conf not in CONFIDENCES:
            fail(f"{country}: invalid confidence '{conf}'")

        check_optional_int(record.get("iaea_milestone_phase"), "iaea_milestone_phase", country, lo=1, hi=3)
        check_optional_int(record.get("commercial_reactors_operating"), "commercial_reactors_operating", country, lo=0)
        check_optional_int(record.get("commercial_reactors_under_construction"), "commercial_reactors_under_construction", country, lo=0)
        check_optional_number(record.get("capacity_gw_planned"), "capacity_gw_planned", country, lo=0)
        check_optional_int(record.get("first_grid_target_year"), "first_grid_target_year", country, lo=1990, hi=2100)
        check_optional_number(record.get("electricity_access_pct"), "electricity_access_pct", country, lo=0, hi=100)
        check_optional_number(record.get("installed_capacity_mw"), "installed_capacity_mw", country, lo=0)

        if record.get("research_reactor") is not None:
            check_string(record.get("research_reactor"), "research_reactor", country)
        check_string(record.get("regulator"), "regulator", country)
        check_string(record.get("implementing_agency"), "implementing_agency", country)
        check_string(record.get("notes"), "notes", country)
        check_string_list(record.get("vendors"), "vendors", country)
        check_string_list(record.get("agreements"), "agreements", country)
        check_string_list(record.get("sources"), "sources", country, min_items=1)

        if not record.get("sources"):
            fail(f"{country}: must have at least one source")
        for src in record.get("sources", []):
            if not str(src).startswith("http"):
                fail(f"{country}: source URL must start with http: {src}")

        for event in record.get("key_events", []):
            if not isinstance(event, dict):
                fail(f"{country}: key_event must be an object")
                continue
            date = event.get("date")
            if not isinstance(date, str) or not DATE_RE.match(date):
                fail(f"{country}: key_event date must be YYYY or YYYY-MM, got '{date}'")
            check_string(event.get("title"), "key_event title", country)
            src = event.get("source")
            if not isinstance(src, str) or not src.startswith("http"):
                fail(f"{country}: key_event source must be a URL starting with http")

        verified = record.get("last_verified")
        if not valid_date(verified):
            fail(f"{country}: last_verified must be an ISO date (YYYY-MM-DD), got '{verified}'")

    check_csv(dataset)

    print_summary(dataset)
    print_errors()
    return 1 if errors else 0


def check_csv(dataset):
    csv_path = DATA / "countries.csv"
    if not csv_path.exists():
        fail("countries.csv: file missing (must exist alongside afrpoweros.json)")
        return
    try:
        with open(csv_path, encoding="utf-8", newline="") as fh:
            rows = list(csv.DictReader(fh))
    except Exception as exc:
        fail(f"countries.csv: cannot read ({exc})")
        return
    if not rows:
        fail("countries.csv: empty file")
        return
    header = set(rows[0].keys())
    for field in CSV_HEADER:
        if field not in header:
            fail(f"countries.csv: missing column '{field}'")

    by_country = {c["country"].lower(): c for c in dataset["countries"]}
    csv_countries = set()
    for row in rows:
        name = row.get("country", "").strip()
        if not name:
            fail("countries.csv: row with empty country")
            continue
        csv_countries.add(name.lower())
        rec = by_country.get(name.lower())
        if rec is None:
            fail(f"countries.csv: '{name}' has no record in afrpoweros.json")
            continue
        for field in CSV_MATCH_FIELDS:
            csv_val = row.get(field, "").strip() or ""
            json_val = rec.get(field)
            if json_val is None:
                json_val = ""
            elif not isinstance(json_val, str):
                json_val = str(json_val)
            if csv_val != json_val:
                fail(f"countries.csv: '{name}' {field} = '{csv_val}' but afrpoweros.json has '{json_val}'")
        csv_region = row.get("region", "").strip()
        if csv_region != rec.get("region"):
            fail(f"countries.csv: '{name}' region = '{csv_region}' but afrpoweros.json has '{rec.get('region')}'")

    for name in by_country:
        if name not in csv_countries:
            fail(f"countries.csv: missing row for '{by_country[name]['country']}'")


def print_summary(dataset):
    statuses = {}
    for rec in dataset["countries"]:
        s = rec["program_status"]
        statuses[s] = statuses.get(s, 0) + 1
    print(f"AfrPowerOS dataset: {len(dataset['countries'])} countries")
    for status in sorted(statuses, key=lambda s: -statuses[s]):
        print(f"  {status:<18} {statuses[status]}")
    print()


def print_errors():
    if not errors:
        print("OK: all checks passed")
        return
    print(f"FAILED: {len(errors)} error(s)", file=sys.stderr)
    for err in errors:
        print(f"  - {err}", file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())
