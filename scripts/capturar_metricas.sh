#!/usr/bin/env bash
set -e

REGISTRO_CSV="data/registro.csv"

echo "=== 🐜 HormigasAIS: Captura de Métricas (Ventana 1h) ==="
echo ""

echo "📌 INSTAGRAM REEL (ID: Dd3dcp9R94d)"
read -p "  └─ Reproducciones / Views: " ig_views
read -p "  └─ Me gusta / Likes: " ig_likes

echo ""
echo "📌 YOUTUBE SHORT (ID: 18PiCYHpgus)"
read -p "  └─ Vistas / Views: " yt_views
read -p "  └─ Me gusta / Likes: " yt_likes

echo ""
echo "⚙️ Registrando en $REGISTRO_CSV..."

scripts/exp.sh medir experiment_id=EXP-001 variant=B platform=Instagram content_id=Dd3dcp9R94d window=1h duration_s=13 views="$ig_views" likes="$ig_likes"
scripts/exp.sh medir experiment_id=EXP-001 variant=B platform=YouTube content_id=18PiCYHpgus window=1h duration_s=13 views="$yt_views" likes="$yt_likes"

echo ""
echo "✅ Métricas guardadas."
tail -n 4 "$REGISTRO_CSV"
