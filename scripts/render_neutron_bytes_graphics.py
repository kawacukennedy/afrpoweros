import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

OUT = "neutron-bytes-graphics"
os.makedirs(OUT, exist_ok=True)

d = json.load(open("data/afrpoweros.json"))
countries = {c["country"]: c for c in d["countries"]}

STATUS_COLOR = {
    "Operating": "#1b5e20",
    "Under Construction": "#b26a00",
    "Preparing": "#2557a7",
    "Exploring": "#90a4ae",
    "None": "#cfd8dc",
}

def save(fig, name):
    png = os.path.join(OUT, name + ".png")
    jpg = os.path.join(OUT, name + ".jpg")
    fig.savefig(png, dpi=200, bbox_inches="tight", facecolor="white")
    fig.savefig(jpg, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", png, "and", jpg)


# Graphic 1: planned capacity with first-grid target, sorted
rows = []
for c, rec in countries.items():
    if rec["capacity_gw_planned"]:
        rows.append((c, rec["capacity_gw_planned"], rec["first_grid_target_year"], rec["program_status"]))
rows.sort(key=lambda r: r[1])
labels = [f"{c} ({yr or 'n/a'})" for c, gw, yr, st in rows]
vals = [gw for c, gw, yr, st in rows]
cols = [STATUS_COLOR[st] for c, gw, yr, st in rows]

fig, ax = plt.subplots(figsize=(8.5, 4.8))
bars = ax.barh(labels, vals, color=cols)
for bar, v in zip(bars, vals):
    ax.text(bar.get_width() + 0.12, bar.get_y() + bar.get_height()/2, f"{v:.1f} GW", va="center", fontsize=9)
ax.set_xlabel("Planned capacity (GW)")
ax.set_xlim(0, max(vals) * 1.28)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="x", linestyle=":", alpha=0.4)
ax.set_title("Planned nuclear capacity by country (first-grid target year)", fontsize=12)
fig.text(0.01, 0.01, "Source: AfrPowerOS open dataset (data/afrpoweros.json), verified 2026-08-16. "
                     "Credit: AfrPowerOS — open, cited data on Africa's civilian nuclear programs. CC BY 4.0.",
         fontsize=7, color="#444")
fig.subplots_adjust(left=0.14, right=0.97, top=0.90, bottom=0.16)
save(fig, "graphic-1-planned-capacity")


# Graphic 2: timeline of key milestones
events = [
    ("2015", "Russia–Egypt IGA (El Dabaa)", "Under Construction"),
    ("2017", "Ghana completes IAEA Phase 1", "Preparing"),
    ("2018", "Kenya completes IAEA Phase 1", "Preparing"),
    ("2019", "Uganda & Tanzania complete Phase 1", "Preparing"),
    ("2022-07", "First concrete at El Dabaa Unit 1", "Under Construction"),
    ("2025-10", "South Africa IRP 2025: 5,200 MW by 2039", "Operating"),
    ("2025-11", "Koeberg Unit 2 licence to 2045", "Operating"),
    ("2026-01", "DR Congo TRICO-II restart approved", "None"),
    ("2026-03", "Kenya targets grid by 2034 (ICONE)", "Preparing"),
    ("2026-03", "Rwanda INIR Phase 2 follow-up", "Preparing"),
]
years = [e[0] for e in events]
texts = [e[1] for e in events]
cols = [STATUS_COLOR[e[2]] for e in events]

fig, ax = plt.subplots(figsize=(10, 5.2))
ax.set_title("Africa's civilian nuclear milestones — key events", fontsize=12)
for i, (yr, tx, st) in enumerate(events):
    ax.bar(i, 1, color=STATUS_COLOR[st], width=0.55)
    ax.text(i, 1.06, yr, ha="center", fontsize=9, fontweight="bold")
    ax.text(i, -0.12, tx, ha="center", va="top", fontsize=7.2, wrap=True, linespacing=1.2,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f5f5f5", edgecolor="#bbbbbb"))
ax.set_xlim(-0.7, len(events) - 0.3)
ax.set_ylim(-1.45, 1.5)
ax.axis("off")
from matplotlib.patches import Patch
leg = [Patch(color=v, label=k) for k, v in STATUS_COLOR.items()]
ax.legend(handles=leg, loc="upper right", fontsize=7, frameon=False, ncol=2)
fig.text(0.01, 0.02, "Source: AfrPowerOS open dataset (data/afrpoweros.json), verified 2026-08-16. "
                     "Each event cites its source URL in the dataset. Credit: AfrPowerOS — CC BY 4.0.",
         fontsize=7, color="#444")
fig.subplots_adjust(left=0.14, right=0.97, top=0.90, bottom=0.16)
save(fig, "graphic-2-milestone-timeline")


# Graphic 3: status scoreboard
from collections import Counter
import numpy as np

status_counts = Counter(c["program_status"] for c in countries.values())
order = ["Exploring", "Preparing", "Under Construction", "Operating", "None"]
counts = [status_counts.get(s, 0) for s in order]
labels = ["Exploring", "Preparing", "Under construction", "Operating", "No program"]
names = {
    "Exploring": "Zambia, Morocco, Algeria, Ethiopia, Tunisia, Zimbabwe, Senegal, Mali, Niger, Eswatini",
    "Preparing": "Rwanda, Kenya, Ghana, Uganda, Tanzania, Nigeria, Sudan",
    "Under Construction": "Egypt (El Dabaa: 4 \u00d7 VVER-1200)",
    "Operating": "South Africa (Koeberg Units 1 & 2)",
    "None": "DR Congo (research reactor restart only)",
}

fig, ax = plt.subplots(figsize=(9, 4.6))
colors = [STATUS_COLOR[s] for s in order]
bars = ax.barh(labels[::-1], counts[::-1], color=colors[::-1])
for bar, cnt in zip(bars, counts[::-1]):
    ax.text(bar.get_width() + 0.15, bar.get_y() + bar.get_height()/2, str(cnt), va="center", fontsize=11, fontweight="bold")
for i, (lbl, cnt, nm) in enumerate(zip(labels[::-1], counts[::-1], [names[s] for s in order[::-1]])):
    ax.text(0.4, bars[i].get_y() + bars[i].get_height()/2 - 0.42, nm, fontsize=6.8, color="#333")
ax.set_xlim(0, max(counts) + 14.5)
ax.set_ylim(-0.5, 4.5)
ax.set_xlabel("Number of countries")
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="x", linestyle=":", alpha=0.4)
ax.set_title("The continental scoreboard — 20 African countries by program status", fontsize=12)
fig.text(0.01, 0.02, "Source: AfrPowerOS open dataset (data/afrpoweros.json), verified 2026-08-16. "
                     "Credit: AfrPowerOS — open, cited data on Africa's civilian nuclear programs. CC BY 4.0.",
         fontsize=7, color="#444")
fig.subplots_adjust(left=0.12, right=0.97, top=0.88, bottom=0.16)
save(fig, "graphic-3-status-scoreboard")