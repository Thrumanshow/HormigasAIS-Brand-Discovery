#!/usr/bin/env bash
set -e

EXP="${1:-EXP-001}"
VAR="${2:-B}"
PLA="${3:-Instagram}"
CID="${4:-Dd3dcp9R94d}"
WIN="${5:-1h}"
DUR="${6:-13}"

echo "=== 🐜 Captura de Metricas: $EXP | Var: $VAR | $PLA ($WIN) ==="
read -p "  └─ Views / Reproducciones: " views
read -p "  └─ Likes / Me gusta: " likes

scripts/exp.sh medir experiment_id="$EXP" variant="$VAR" platform="$PLA" content_id="$CID" window="$WIN" duration_s="$DUR" views="$views" likes="$likes"

echo "✅ Metrica registrada."