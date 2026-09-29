#!/usr/bin/env bash
ID_EXP="${1}"
VENTANA="${2}"

if [ -z "$ID_EXP" ] || [ -z "$VENTANA" ]; then
    echo "❌ Uso: scripts/exp.sh capturar [ID_EXP] [VENTANA]"
    echo "👉 Ejemplo: scripts/exp.sh capturar EXP-002-A 1h"
    exit 1
fi

echo "🐜 ======================================================="
echo "   RECOLECTOR IMPARCIAL DE MÉTRICAS - NODO A16@Soberano"
echo "   Experimento: $ID_EXP | Ventana: $VENTANA"
echo "   (Presiona ENTER si un dato no está disponible)"
echo "======================================================="

read -p "🌐 Plataforma (ej. YouTube / Instagram): " PLATAFORMA
read -p "📊 Vistas (views): " VIEWS
read -p "❤️ Me Gusta (likes): " LIKES
read -p "💬 Comentarios (comments): " COMMENTS
read -p "🔄 Compartidos (shares): " SHARES
read -p "🔖 Guardados (saves): " SAVES

python3 scripts/add_row.py \
  "experiment_id=$ID_EXP" \
  "window=$VENTANA" \
  "platform=$PLATAFORMA" \
  "views=$VIEWS" \
  "likes=$LIKES" \
  "comments=$COMMENTS" \
  "shares=$SHARES" \
  "saves=$SAVES"
