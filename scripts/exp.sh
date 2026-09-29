#!/usr/bin/env bash
case "$1" in
  issues)   gh issue list --state all ;;
  ver)      gh issue view "$2" ;;
  nota)     gh issue comment "$2" --body "$3" ;;
  nuevo)    python3 scripts/crear_hipotesis.py "${@:2}" ;;
  medir)    python3 scripts/add_row.py "${@:2}" ;;
  capturar) scripts/capturar_metricas.sh "${@:2}" ;;
  validar)  python3 scripts/validar_registro.py "${@:2}" ;;
  analizar) python3 scripts/analizar.py ;;
  sync)     git pull --rebase && git status -sb ;;
  subir)    git add -A && git commit -m "$2" && git push ;;
  *) echo "Uso: exp.sh issues | ver N | nota N \"texto\" | nuevo [ID VAR PLAT HIP] | medir ... | capturar ... | validar | analizar | sync | subir \"msg\"" ;;
esac
