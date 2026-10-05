import csv, datetime

def t(s):
    try:
        return datetime.datetime.fromisoformat(s)
    except Exception:
        return None

pub = {}
with open("data/publicaciones.csv", newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        pub[r["content_id"]] = t(r["published_at"])

with open("data/registro.csv", newline="", encoding="utf-8") as f:
    rows = [r for r in csv.DictReader(f) if r["views"] != "unknown"]

print("video        plat  var  captura           horas vistas likes comp shar")
for r in rows:
    c, p = t(r["captured_at"]), pub.get(r["content_id"])
    h = "%.0f" % ((c - p).total_seconds() / 3600) if c and p else r["window"]
    print("%-12s %-5s %-4s %-17s %5s %6s %5s %4s %4s" % (
        r["content_id"][:12], r["platform"][:5], r["variant"][:4],
        r["captured_at"][:16].replace("T", " "), h,
        r["views"], r["likes"], r["comments"], r["shares"]))
