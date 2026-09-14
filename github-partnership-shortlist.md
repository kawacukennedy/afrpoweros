# GitHub Partnership Shortlist — Zero-Cost, High-Leverage

Searched via `gh` (Sep 2026). Goal: free partnerships that bring users,
credibility, or data-consumers to AfrPowerOS with no money spent.

Ranked by leverage ÷ effort. All are no-cost (PRs, open issues, public
directories — no paid inclusion anywhere).

---

## Outcome table (updated 2026-09-09)

| # | Target | Issue/PR | Status | Outcome |
|---|--------|----------|--------|---------|
| 6 | apd-core / awesome-public-datasets | [PR #647](https://github.com/awesomedata/apd-core/pull/647) | **MERGED 2026-09-08** | WIN — entry live on awesome-public-datasets (78,836★), line 605 of README.rst |
| 3 | protontypes/open-sustainable-technology | [#1636](https://github.com/protontypes/open-sustainable-technology/pull/1636), [#1637](https://github.com/protontypes/open-sustainable-technology/pull/1637) | Closed twice by maintainer | MISS — maintainer declined twice silently; posted one follow-up asking blocker, will not reopen again |
| 1 | kaykluz/africa-energy-software-map | [#96](https://github.com/kaykluz/africa-energy-software-map/issues/96) | OPEN, awaiting review | PENDING — awaiting editorial intake |
| 2 | CodeForAfrica / openAFRICA | [#58](https://github.com/CodeForAfrica/openAFRICA/issues/58) | OPEN, awaiting review | PENDING — ties into CfA dev emails in flight |
| 4 | PyPSA-Earth | [#2026](https://github.com/pypsa-meets-earth/pypsa-earth/discussions/2026) | OPEN | PENDING — awaiting maintainer response |
| 5 | GeoNuclearData | [#6](https://github.com/cristianst85/GeoNuclearData/issues/6) | OPEN, awaiting response | PENDING — low priority; maintainer unresponsive (last push 2024-03) |
| 8 | BiaPri/awesome-energy-tools | [PR #1](https://github.com/BiaPri/awesome-energy-tools/pull/1) | OPEN, awaiting review | PENDING — small repo (15★), low leverage |
| 7 | bytewax/awesome-public-real-time-datasets | n/a | SKIPPED | WRONG FIT — AfrPowerOS is a cadence-released static dataset, not a real-time stream; skipped to preserve honesty |

---

## Tier 1 — Act on these first

### 1. Africa Energy Software Map (kaykluz/africa-energy-software-map)
- **What:** Open, evidence-backed directory of software + companies across
  Africa's energy value chain. Live map at map.kaykluz.com. Explicitly "No paid
  ranking, paid verification, or paid inclusion." Active (pushed 2026-09-02),
  MIT data license, CC BY 4.0 dataset. 528 software records, 2,265 companies.
- **Fit:** Perfect. AfrPowerOS is exactly a "software/infrastructure product"
  of the kind it indexes.
- **Action taken:** Issue #96 opened (2026-09-07) using `new-solution.yml` form
  fields — full product name, description, African deployment, source URL,
  relationship disclosed as "Provider or employee."
- **Status:** Open, awaiting editorial intake. No response yet.
- **Cost:** 0. **Effort:** Low — one issue form.

### 2. openAFRICA (CodeForAfrica/openAFRICA) — open.africa
- **What:** "The continent's largest volunteer-driven open data portal"
  (CKAN), run by Code for Africa. 33★.
- **Fit:** Strong. We already have outreach in flight to Code for Africa devs
  (Stephane Njoki, Gideon Maina). A dataset entry on the continent's own open
  data portal is high-credibility and reaches African civic/data users directly.
- **Action taken:** Issue #58 opened (2026-09-07) proposing dataset publication
  + partnership. Detailed the dataset, offered CSV/JSON, asked about submission
  flow and quality requirements.
- **Status:** Open, awaiting review. Ties into in-flight CfA dev emails.
- **Cost:** 0. **Effort:** Low–med (CKAN submission / account still needed).

### 3. protontypes/open-sustainable-technology (2,546★) — MISSED
- **What:** Flagship directory of open-source software for climate/sustainable
  energy/biodiversity. CC BY 4.0. Actively maintained. Explicit PR/issue
  contribution path.
- **Action taken:** PR #1636 opened (2026-09-07), closed by maintainer (Tobias
  Augspurger) — root cause: `readme` API returned truncated 512K blob; real
  file is 537K, so pushed file corrupted tail sections. PR #1637 resubmitted
  with corrected branch (single-line diff verified via `gh pr diff`). CI ran
  `action_required` (first-time contributor approval gate) but maintainer closed
  #1637 without explanation on 2026-09-08. Posted one polite follow-up comment
  asking if there's a specific blocker — will not reopen a third time.
- **Status:** CLOSED. Maintainer declined twice; respect the outcome.
- **Key learning:** Never trust `gh api .../readme --jq .content` for large
  repos — the response may be truncated. Always use `gh api
  repos/.../contents/README.md` for the full authoritative blob.

### 4. PyPSA-Earth (pypsa-meets-earth/pypsa-earth, 364★)
- **What:** PyPSA's whole-continent open optimization model for energy futures —
  actively used for African energy modeling (there's even a pypsa-africa-hackathon).
- **Fit:** A genuine *data consumer* partner, not just a directory. PyPSA's African
  work is fuel-starved for exactly the country-level nuclear/energy facts AfrPowerOS
  carries.
- **Action taken:** Discussion #2026 opened (2026-09-07) under "Ideas" category.
  Proposed AfrPowerOS as a cited input/cross-reference layer for African
  country data — nuclear program status, installed capacity, generation mix,
  electricity access. Offered clean CSV/JSON export. Asked maintainer preference
  on delivery and licensing.
- **Status:** Open, awaiting maintainer response.
- **Cost:** 0. **Effort:** Med (next: follow up if no response within 7 days).

---

## Tier 2 — Good but lower leverage

### 5. GeoNuclearData (cristianst85/GeoNuclearData, 59★)
- **What:** Worldwide nuclear power plant database (reactor-level, JSON/CSV/MySQL).
  Actively used. Stalled updates (last push 2024-03) but long-lived/established.
- **Fit:** Topical but complementary — it's global reactor inventory; we're
  Africa program/infrastructure intelligence.
- **Action taken:** Issue #6 opened (2026-09-07) proposing link-only cross-link
  (respecting their NOASSERTION license — no data copying). Offered to cite
  GeoNuclearData's African reactors in AfrPowerOS and vice versa.
- **Status:** Open, awaiting response. Maintainer inactive since 2024-03 — may
  not respond.
- **Cost:** 0. **Effort:** Med (only if maintainer engages).

### 6. awesomedata/awesome-public-datasets (78,836★) — MERGED ✓
- **What:** The giant curated list of open datasets (topic-centric, 78k+★).
- **Action taken:** Forked `apd-core` → `core/Energy/AfrPowerOS.yml` created
  (2026-09-07) using correct YAML template (title, homepage, category, description,
  license, language, organization). PR #647 opened.
- **Status:** MERGED 2026-09-08 by ppival. Auto-deployed to main list —
  AfrPowerOS live at line 605 of `awesome-public-datasets` README.rst.
- **Note:** Contribution must go to `awesomedata/apd-core` (not to the main
  awesome-public-datasets repo), since the list is auto-generated from YAML
  entries via deploy pipeline.

### 7. BiaPri/awesome-energy-tools (15★)
- **What:** Energy datasets & tools hub (datasets + tools categories).
- **Action taken:** Forked → README edited to add new "Electricity Generation &
  Access" subsection under Datasets; PR #1 opened (2026-09-07).
- **Status:** OPEN, awaiting review.
- **Cost:** 0. **Effort:** Low.

---

## Tier 3 — Watch / on-topic but not actionable now

- **calliope-project/calliope (373★)** — energy modeling framework (could consume
  data like PyPSA-Earth; secondary).
- **CodeForAfrica/PesaYetu, dsfsi/dsfsi-datasets** — data/civic infrastructure,
  more for future CfA collaboration than a listing.
- Many 0-star Africa energy scraping projects — student work, high effort, little
  network effect; skip unless a specific contact wants to cross-link.

---

## Operating notes

- **AGENTS.md hard rule 1:** Every record must have a source URL + confidence
  label. No fabricated data, sources, or dates. All outreach messages state
  facts verifiable from our live repo/site.
- **No paid inclusion:** All targets above explicitly offer free listings. We did
  not and will not pay for any entry.
- **Ecosyste.ms timing:** `repos.ecosyste.ms` syncs new repos asynchronously.
  If a bot calls it within hours of fork creation, data may not be available yet.
  The OST review bot posted "Could not fetch" on our PR precisely because our
  repo hadn't been indexed at PR-creation time. Verify `repos.ecosyste.ms` lookup
  returns data before creating PRs on OST-type directories.
- **GitHub readme API truncation (ost lesson):** `gh api .../readme --jq .content`
  may return a truncated response for very large files (>500KB). Always use
  `gh api repos/.../contents/README.md` for the authoritative blob when
  building PRs from upstream READMEs.
