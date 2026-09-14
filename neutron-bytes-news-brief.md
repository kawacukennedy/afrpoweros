# Neutron Bytes — Option 1 brief (send-ready)

Pastable news brief for Dan Yurman. All facts taken from `data/afrpoweros.json`
(every record cited + confidence-labelled; full source URLs below). No invented figures.

---

**Headline suggestion:** "Africa's nuclear buildout, by the numbers"

**Nut graf:** AfrPowerOS, an open dataset tracking every African country's civilian
nuclear program, now covers 20 countries — every record cited and confidence-labelled.
The picture: one country operating, one building Africa's first new nuclear plant in
decades, seven preparing, ten exploring.

---

## Top-line numbers (20 countries)

| Status | Count |
|---|---|
| Exploring | 10 |
| Preparing (IAEA Phase 2) | 7 |
| Under construction (Phase 3) | 1 |
| Operating (Phase 3) | 1 |
| No program tracked | 1 (DR Congo — research reactor restart only) |

Only South Africa operates a commercial NPP in Africa today (Koeberg).

---

## Three country snapshots

### Kenya — Preparing (IAEA Phase 2)
- ~2,000 MW planned; first grid target **2034**, announced at ICONE 2026 (Nairobi).
- Completed IAEA Phase 1 (2018); IAEA SEED site-evaluation mission (2024).
- Site and vendor not yet selected.
- Sources: world-nuclear-news.org/articles/kenya-agency-outlines-nuclear-development-plans
  (Verified); kenyanews.net/news/278943804/intl-nuclear-energy-forum-opens-in-kenya-amid-call-for-safety
  (planned capacity, Unverified).

### Egypt — Under construction (IAEA Phase 3)
- El Dabaa: **4 × VVER-1200** under construction on the Mediterranean coast (Rosatom).
- First concrete July 2022; **Unit 1 grid connection ~2028**, all four units ~2030.
- 4.8 GW planned; Russia–Egypt intergovernmental agreement (2015); Russian state loan
  facility (~USD 25 billion).
- Africa's first new nuclear build in decades.
- Sources: world-nuclear-news.org/articles/construction-of-egypts-first-nuclear-power-plant-u
  and .../supplementary-agreements-signed-for-el-dabaa-project; tass.com/economy/2177563
  (2028 target).

### South Africa — Operating (IAEA Phase 3)
- Koeberg Units 1 & 2 operating — 1,860 MW net; only operating commercial NPP in Africa.
- IRP 2025 (approved Oct 2025): **5,200 MW new nuclear by 2039**; initial 1,200 MW
  targeted 2036.
- Koeberg Unit 2 licence extended to 2045 (Nov 2025); procurement route not finalised.
- Sources: world-nuclear-news.org/articles/south-african-government-approves-draft-2025-irp;
  .../koeberg-unit-2-approved-for-extended-operation.

---

## Useful color (in the dataset)
- DR Congo: no commercial program, but IAEA TC project COD1014 (Jan 2026) backs restarting
  the TRICO-II research reactor at CREN-K (iaea.org/projects/tc/cod1014).
- Per-country fields include: IAEA milestone phase, reactors operating/under construction,
  planned GW, first-grid target year, research reactors, regulator, implementing agency,
  vendors, agreements, electricity access %, dated+sourced key events.

## Raw data for verification
- Dataset site: https://kawacukennedy.github.io/afrpoweros/
- JSON: https://github.com/kawacukennedy/afrpoweros/blob/main/data/afrpoweros.json
- CSV: https://github.com/kawacukennedy/afrpoweros/blob/main/data/countries.csv
- Repo: https://github.com/kawacukennedy/afrpoweros

---

## Not for publication — private notes
- Option 2 (deeper piece): offer full JSON+CSV, methodology (docs/methodology.md),
  schema (data/schema.json), and Q&A on any record.
- Option 3 (lightest): one-line reading-list pointer, e.g. "AfrPowerOS — cited, open
  dataset on civilian nuclear programs across 20 African countries: github.com/kawacukennedy/afrpoweros".