import csv, sys

path = "data/registro.csv"
with open(path, newline="", encoding="utf-8") as f:
    header = next(csv.reader(f))

vals = dict(a.split("=", 1) for a in sys.argv[1:])
bad = [k for k in vals if k not in header]
if bad:
    sys.exit("Columnas desconocidas: " + ", ".join(bad))

row = [vals.get(c, "unknown") for c in header]
with open(path, "a", newline="", encoding="utf-8") as f:
    csv.writer(f, lineterminator="\n").writerow(row)
print("Fila añadida:", row[:6])
