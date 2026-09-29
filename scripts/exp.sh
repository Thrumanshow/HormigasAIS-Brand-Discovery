#!/usr/bin/env bash
cd "$(dirname "$0")/.." || exit 1
case "$1" in
  issues) gh issue list --state all ;;
  ver)    gh issue view "$2" ;;
  nota)   gh issue comment "$2" --body "$3" ;;
  medir)  python scripts/add_row.py "${@:2}" ;;
  sync)   git pull --rebase && git status -sb ;;
  subir)  git add -A && git commit -m "$2" && git push ;;
  *) echo "Uso: exp.sh issues | ver N | nota N 'texto' | medir col=valor ... | sync | subir 'mensaje'" ;;
esac
