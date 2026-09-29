import csv, sys

path = "data/registro.csv"
if len(sys.argv) < 3:
    sys.exit("Uso: python scripts/set_row.py CONTENT_ID columna=valor ...")

cid = sys.argv[1]
changes = dict(a.split("=", 1) for a in sys.argv[2:])

with open(path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)

hits = 0
for r in rows:
    if r["content_id"] == cid:
        for k, v in changes.items():
            if k not in r:
                sys.exit("Columna desconocida: " + k)
            r[k] = v
        hits += 1

if not hits:
    sys.exit("content_id no encontrado: " + cid)

with open(path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

print("Filas actualizadas:", hits)
