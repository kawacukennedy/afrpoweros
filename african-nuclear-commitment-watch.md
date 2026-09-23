# African Nuclear Commitment Watch List — for Neutron Bytes News Notes

**Purpose:** Monitor African civilian nuclear programs for *real commitments* — signed
contracts, EPC deals, vendor selections, first concrete/first pour — **not MoUs or LOIs**.
When something solid lands, draft a ≤700-word news note and submit to Dan Yurman (Neutron
Bytes) with byline, per his standing invitation (Sep 13, 2026).

**Submission rules (from Dan, verbatim intent):**
- News notes ≤ **700 words**; byline: *"Special to Neutron Bytes by Kennedy Kawacu"* with
  email + website URL at the end of the item.
- Graphics only if simple and legible at a glance ("16 pt+ fonts, simple").
- No compensation; evergreen framing; cite primary sources.
- Format example: `[Title] African Country commits to build SMRs with (vendor) and (firm) as EPC`.
- Submit only for **real commitments, not MOUs**. Confirm with a primary source
  (company/Eskom/government statement, NNR, contract award notice) before drafting.

---

## Watch status of tracked countries (from `data/afrpoweros.json`, Sep 2026)

### RED — closest to a real commitment (monitor weekly)
- **Ghana** — selected NuScale/Regnum (US) and CNNC (CN) as vendors for its first nuclear
  plants in March 2025, signing framework agreements (no formal construction contract yet).
  Plans ~1 GW of nuclear on the grid by 2034. Next move: **site evaluation / contract award**.
  This is the single most likely near-term story.
- **Rwanda** — Dual Fluid Energy and Rosatom agreements on record; Rwanda targets ~1 GW.
  Watch for **construction start, site works, or firm order** (not partnership MoUs).
- **Egypt (El Dabaa)** — Rosatom EPC contract already signed; Unit 1 first concrete July
  2022, ~2028 first grid; **four units under construction**. No big news-note trigger unless
  milestone events occur (first fuel load, cold/hot tests, NPPC progress) — but a
  construction-phase update is a valid news item on advancement.

### AMBER — active procurement / feasibility program (monitor monthly)
- **Kenya** — first plant ~2,000 MW (KenGen–NuPEA MoU, Dec 2025, scaling to 6,000 MW);
  IAEA Phase 2; first grid ~2034. Watch for **vendor selection** (no vendors on record yet).
- **Nigeria** — ~4,000 MW planned in Phase 2; watch for **vendor selection / NRC licensing
  progress** (Rosatom announcements and China MoUs on record).
- **Uganda** — vision of 8,400 MW planned; watch for **vendor/financial agreement**.
- **Tanzania** — assessing vendors; watch for **contract award**.
- **Sudan** — 4 agreements incl. Russia; treat with caution (political/security context),
  verify any claim against primary sources.
- **Morocco, Algeria, Tunisia, Ethiopia, Senegal** — exploration/feasibility; watch for
  **milestone "commitment"** (agreement on financing, vendor, or site). Algeria has Rosatom
  SMR feasibility discussions on record.

### GREEN — watch for unexpected movement only
- **Zimbabwe** (KHNP i-SMR evaluation MoU — MoU, not commitment), **Zambia** (1,000 MW
  target, no vendors), **Mali, Niger, Eswatini, DR Congo** (early stage), **South Africa**
  (Koeberg operating; watch IRP 2025 new-build procurement → vendor selection = major story).

---

## Sources to monitor (check frequency)
1. **World Nuclear News (WNN)** — https://www.world-nuclear-news.org/ (daily)
2. **Reuters Energy** — https://www.reuters.com/business/energy/ (daily)
3. **Nuclear Engineering International** — https://www.neimagazine.com/ (weekly)
4. **IAEA PRIS** — https://pris.iaea.org/PRIS/home.aspx (weekly; unit/construction data)
5. **Per-country primary sources:**
   - Eskom / NNR (South Africa) — eskom.co.za, nnr.co.za
   - Ghana Nuclear Power Organisation (Ghana)
   - Ministry/Ministry-commission statements (Kenya NUPEA/EPRA, Nigeria NRC, Uganda)
   - Vendor press releases: Rosatom, EDF, KHNP/KEPCO, CNNC/CGN, NuScale, Dual Fluid,
     GE-Hitachi, OPG/Laurentis, and country utility announcements
6. **IAEA topical news** — https://www.iaea.org/newscenter/news (weekly)
7. Optional: Power Africa / US DOE Africa program updates, and regional outlets.

---

## News-note triggers (what qualifies as a "real commitment")
- **Signed EPC / construction contract** (vendor + EPC firm named).
- **Vendor selection / preferred-bidder award** in a formal tender.
- **First concrete / first pour / construction start** at a committed site.
- **First fuel load** or commercial operation milestone.
- **Final Investment Decision (FID)** announced for a project.
- **Financing closed** (export credit, sovereign guarantee, funding agreement).

**Does NOT qualify on its own:** MoUs, LOIs, letters of intent, cooperation
frameworks, capacity-building agreements, feasibility studies, roadmap publications.

---

## Draft template (≤700 words)

```
[Title] <Country> commits to build <reactor type> with <vendor> as <EPC>

Special to Neutron Bytes by Kennedy Kawacu
kawacukent@gmail.com | https://kawacukennedy.github.io/afrpoweros/

<Lead: the commitment, date, amount/capacity>
<Context: program stage, prior MoUs, regulatory/licensing status>
<Details: vendor, EPC, location, timeline, capacity>
<Source links: primary statements + 1-2 reputable secondary>

— Kennedy Kawacu | AfrPowerOS: Open, cited intelligence on African nuclear
  & energy infrastructure (kawacukent@gmail.com, https://github.com/kawacukennedy/afrpoweros)
```

---

## Standby list (already-written angles, in case of comments/interest)
- Koeberg incidents summary (4 INES Level 0 events, Jul 2026) — compiled, not yet submitted.
- "Africa's Nuclear Buildout, by the Numbers" — published Sep 11, 2026 on Neutron Bytes.
- Togo as 21st tracked country (Atomic Energy Commission, IAEA framework, NEISA 2027 host).

---

## Process
1. **Scan** sources (daily/weekly cadence above).
2. **Verify** any commitment against a primary source; if confirmed, log an entry.
3. **Draft** a ≤700-word note using the template.
4. **Submit** to Dan via email (neutronbytes@gmail.com; also on Signal/cell 216-369-7194
   if urgent). Note: Dan is **away Sep 15–28, 2026** — hold non-urgent submissions until he
   returns unless something breaks hard.
5. **Update the dataset** (`data/afrpoweros.json`) for any newly confirmed commitment,
   run `python3 scripts/validate.py`, and add a CHANGELOG entry.
6. **Track in this file** — log each watchfinding with date, country, trigger, source, status
   (monitoring / submitted / published).