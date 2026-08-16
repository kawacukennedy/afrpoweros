# Data model

The dataset is `data/afrpoweros.json` (JSON, one object per country) plus a flat
summary `data/countries.csv`. `data/schema.json` is the machine-readable JSON
Schema. All three must stay consistent — `scripts/validate.py` enforces this.

## Top-level document

| Field | Type | Notes |
|---|---|---|
| `schema_version` | string | Version of the schema the file conforms to. |
| `generated` | string | ISO date the file was generated/last regenerated. |
| `countries` | array | One entry per country. |

## Country record

| Field | Type | Notes |
|---|---|---|
| `country` | string | Country name (unique). |
| `region` | enum | East / West / North / Central / Southern Africa. |
| `program_status` | enum | `Operating`, `Under Construction`, `Announced`, `Preparing`, `Exploring`, `None`. |
| `iaea_milestone_phase` | int \| null | IAEA "milestones" phase, 1–3. Null when not started. |
| `commercial_reactors_operating` | int | Operating commercial reactors. |
| `commercial_reactors_under_construction` | int | Commercial reactors under construction. |
| `capacity_gw_planned` | number \| null | Announced/planned new capacity in GW(e). Null if no credible figure. |
| `first_grid_target_year` | int \| null | Announced target year for first grid connection. Null if none. |
| `research_reactor` | string \| null | Operating research reactors (name + power/type). |
| `regulator` | string | Nuclear regulator (or nuclear authority where regulator not separated). |
| `implementing_agency` | string | Government body running the nuclear program. |
| `vendors` | array | Vendors in discussion/selection for the program. |
| `agreements` | array | Intergovernmental/cooperation agreements relevant to the program. |
| `electricity_access_pct` | number \| null | Approximate national electricity access rate (%). |
| `installed_capacity_mw` | number \| null | Approximate national installed generation capacity (MW). |
| `notes` | string | Free-text context; the place for nuance and caveats. |
| `key_events` | array | Notable program milestones: `{date, title, source}`. |
| `sources` | array | Source URLs supporting the record (at least one, http(s)). |
| `confidence` | enum | `Verified`, `Inference`, `Speculation`, `Unverified` — see methodology. |
| `last_verified` | string | ISO date the record was last checked against sources. |

## CSV columns

`country, region, program_status, iaea_milestone_phase, capacity_gw_planned,
first_grid_target_year, regulator, implementing_agency, research_reactor,
confidence, last_verified`

The CSV is a subset of the JSON. The validator checks that every CSV row exists
in the JSON and that the overlapping columns match exactly.

## Versioning

Dataset changes follow the repo's Semantic Versioning:

- **Major** — breaking schema change or methodology change.
- **Minor** — new countries, new fields, new event types (backwards compatible).
- **Patch** — corrections and new events for existing records.

The `generated` date and `last_verified` per record should be bumped whenever
the data is touched, so consumers can tell how fresh a record is.
