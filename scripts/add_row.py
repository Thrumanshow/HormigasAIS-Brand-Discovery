import csv, sys, datetime

path = "data/registro.csv"
with open(path, newline="", encoding="utf-8") as f:
    header = next(csv.reader(f))

vals = dict(a.split("=", 1) for a in sys.argv[1:])
vals.setdefault("window", "snapshot")
vals.setdefault("captured_at", datetime.datetime.now().astimezone().isoformat(timespec="seconds"))

bad = [k for k in vals if k not in header]
if bad:
    sys.exit("Columnas desconocidas: " + ", ".join(bad))
ph = [k for k, v in vals.items() if v.upper() in ("NN", "VALOR")]
if ph:
    sys.exit("Marcador sin reemplazar en: " + ", ".join(ph))

row = [vals.get(c, "unknown") for c in header]
with open(path, "a", newline="", encoding="utf-8") as f:
    csv.writer(f, lineterminator="\n").writerow(row)
print("Fila añadida:", row[:7])
