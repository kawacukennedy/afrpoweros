#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def main():
    with open(DATA / "afrpoweros.json", encoding="utf-8") as fh:
        dataset = json.load(fh)

    print(f"AfrPowerOS — {len(dataset['countries'])} countries\n")
    print(f"{'Country':<14}{'Status':<18}{'Phase':<7}{'GW planned':<11}{'Target':<7}Regulator")
    for rec in sorted(dataset["countries"], key=lambda c: c["country"]):
        phase = rec["iaea_milestone_phase"] if rec["iaea_milestone_phase"] else "-"
        gw = rec["capacity_gw_planned"] if rec["capacity_gw_planned"] is not None else "-"
        target = rec["first_grid_target_year"] if rec["first_grid_target_year"] else "-"
        print(
            f"{rec['country']:<14}{rec['program_status']:<18}{phase:<7}"
            f"{str(gw):<11}{str(target):<7}{rec['regulator']}"
        )


if __name__ == "__main__":
    main()
