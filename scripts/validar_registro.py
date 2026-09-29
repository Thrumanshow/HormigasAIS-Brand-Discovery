#!/usr/bin/env python3
import csv, sys
from pathlib import Path
from collections import Counter

PATH = Path("data/registro.csv")

def load():
    with PATH.open("r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)

def validate(fields, rows):
    errors = []
    keys = Counter((r.get("content_id"), r.get("window"), r.get("platform")) for r in rows)
    for k, c in keys.items():
        if c > 1 and None not in k:
            errors.append(f"Duplicado: content_id={k[0]} window={k[1]} platform={k[2]} ({c} veces)")
    return errors

def normalize(rows):
    for r in rows:
        eid = r.get("experiment_id", "")
        if eid in ("EXP001", "EXP-001", "EXP_001"):
            r["experiment_id"] = "EXP-001"
        elif eid in ("EXP000", "EXP-000"):
            r["experiment_id"] = "EXP-000"
        p = r.get("platform", "")
        if p.lower() == "youtube":
            r["platform"] = "YouTube"
        elif p.lower() == "instagram":
            r["platform"] = "Instagram"
        for col in r:
            if r[col] in ("NN", "N/A", "na", ""):
                r[col] = "unknown"
    return rows

def save(fields, rows):
    with PATH.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

def main():
    if not PATH.exists():
        print("No existe data/registro.csv")
        sys.exit(1)
    fields, rows = load()
    print(f"Filas leidas: {len(rows)}")
    errors = validate(fields, rows)
    if errors:
        print("\n⚠️  Problemas encontrados:")
        for e in errors:
            print("  -", e)
    else:
        print("✅ Estructura basica OK")
    if "--fix" in sys.argv:
        rows = normalize(rows)
        save(fields, rows)
        print("🔧 Normalizacion aplicada y guardada.")
    else:
        print("\nEjecuta con --fix para normalizar IDs y valores NN/vacios.")

if __name__ == "__main__":
    main()
