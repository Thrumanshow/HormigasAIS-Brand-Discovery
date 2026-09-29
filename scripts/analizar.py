#!/usr/bin/env python3
import csv, sys
from pathlib import Path
from collections import defaultdict

PATH = Path("data/registro.csv")

def safe_int(v):
    try:
        return int(v)
    except (ValueError, TypeError):
        return None

def main():
    if not PATH.exists():
        print("No existe data/registro.csv")
        sys.exit(1)
    with PATH.open("r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("El registro esta vacio.")
        return
    groups = defaultdict(list)
    for r in rows:
        key = (r.get("experiment_id", "?"), r.get("variant", "?"), r.get("platform", "?"), r.get("window", "?"))
        groups[key].append(r)
    print(f"\n{"EXP":<8} {"VAR":<5} {"PLATAFORMA":<11} {"WIN":<5} {"VIEWS":>7} {"LIKES":>6}")
    print("-" * 50)
    for key in sorted(groups.keys()):
        rows_g = groups[key]
        views = [v for r in rows_g if (v := safe_int(r.get("views"))) is not None]
        likes = [l for r in rows_g if (l := safe_int(r.get("likes"))) is not None]
        v_str = f"{views[-1]}" if views else "-"
        l_str = f"{likes[-1]}" if likes else "-"
        print(f"{key[0]:<8} {key[1]:<5} {key[2]:<11} {key[3]:<5} {v_str:>7} {l_str:>6}")

if __name__ == "__main__":
    main()
