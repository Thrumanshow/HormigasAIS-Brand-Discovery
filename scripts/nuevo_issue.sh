#!/usr/bin/env bash
# Uso: scripts/nuevo_issue.sh EXP VARIANTE PLATAFORMA ID_O_URL [DURACION_S] [FECHA_HORA]
# Ejemplo: scripts/nuevo_issue.sh 001 B YouTube ID_DEL_VIDEO 13
# DRY=1 muestra el cuerpo sin crear el Issue.
set -euo pipefail
cd "$(dirname "$0")/.."

if [ $# -lt 4 ]; then
  echo "Uso: $0 EXP VARIANTE PLATAFORMA ID_O_URL [DURACION_S] [FECHA_HORA]"
  exit 1
fi

EXP=$1; VAR=$2; PLAT=$3
CID=$(printf '%s' "$4" | sed -E 's#.*/(shorts|reel)/##; s#[/?].*##')
DUR=${5:-13}
WHEN=${6:-pendiente}
PROMPT='A16@Soberano:~/HormigasAIS-Brand-Discovery'

case "$PLAT" in
  YouTube|youtube|yt) PLAT=YouTube; SHORT=YT; URL="https://youtube.com/shorts/$CID" ;;
  Instagram|instagram|ig) PLAT=Instagram; SHORT=IG; URL="https://www.instagram.com/reel/$CID/" ;;
  *) echo "Plataforma no válida: use YouTube o Instagram"; exit 1 ;;
esac

if ! printf '%s' "$CID" | grep -Eq '^[A-Za-z0-9_-]{6,15}$'; then
  echo "ID no válido: $CID"; exit 1
fi

TITLE="[VIDEO] EXP${EXP}-${VAR}-${SHORT}"
BODY=$(mktemp "$HOME/.issue.XXXXXX")
trap 'rm -f "$BODY"' EXIT

cat > "$BODY" << BODYEOF
## Identificación
- Experimento: ${EXP}
- Variante: ${VAR}, plataforma ${PLAT}
- Tema: terminal de Termux con el prompt del proyecto (\`${PROMPT}\`)
- Duración (s): ${DUR}

## Publicación
- ${PLAT}: ${URL} (ID \`${CID}\`)
- Fecha y hora: ${WHEN}
- Texto publicado: literal en \`experiments/experiment-${EXP}-brand-text/captions.md\`

## Desviaciones
- Ninguna registrada

## Seguimiento continuo (capturas en cualquier momento; ver con scripts/exp.sh estado)

## Notas
BODYEOF

if [ "${DRY:-0}" = "1" ]; then
  echo "== $TITLE"; cat "$BODY"; exit 0
fi

if [ "$(gh issue list --state all --search "\"$TITLE\" in:title" --json number --jq length)" != "0" ]; then
  echo "Ya existe un Issue con el título: $TITLE"; exit 1
fi

gh issue create --title "$TITLE" --label publicacion --body-file "$BODY"
