#!/usr/bin/env python3
import subprocess
import sys

def inyectar_experimento_gh(id_exp, variable, plataforma, hipotesis):
    """
    Evolución HormigasAIS: Crea un Issue estructurado en GitHub usando 'gh CLI'
    para auditar experimentos de posicionamiento orgánico ampliado.
    """
    titulo = f"🧪 {id_exp}: Evaluación de {variable} en {plataforma}"
    
    cuerpo = f"""# 🐜 Protocolo de Descubrimiento de Marca - HormigasAIS

## 📋 Descripción del Experimento
* **ID:** `{id_exp}`
* **Plataforma Objetivo:** {plataforma}
* **Variable Crítica a Modificar:** `{variable}`

## 🎯 Hipótesis Operativa (Alcance Ampliado)
{hipotesis}

## 📊 Ventanas de Control Cronológico (UTC-6)
- [ ] **T+1h:** Medición de tracción inicial (Ejecutar scripts/validar_registro.py).
- [ ] **T+24h:** Evaluación del empuje del algoritmo secundario en feeds de no-seguidores.
- [ ] **T+72h:** Estabilización de la curva de retención orgánica.
- [ ] **T+7d:** Consolidación de autoridad de marca y conversión estática.

## 🛠️ Instrucciones de Ejecución
1. Modificar **únicamente** la variable `{variable}` en el próximo contenido corto.
2. Registrar datos en `data/registro.csv`.
3. Ejecutar `scripts/exp.sh subir "{id_exp}: Actualización de métricas"` en cada ventana.
"""

    comando = [
        "gh", "issue", "create",
        "--title", titulo,
        "--body", cuerpo,
        "--label", "experimento,crecimiento-organico"
    ]
    
    try:
        print(f"🐜 Conectando con GitHub desde el nodo Soberano...")
        resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
        print(f"✅ [ÉXITO] Issue creado en el repositorio.")
        print(resultado.stdout)
    except FileNotFoundError:
        print("❌ [ERROR] GitHub CLI ('gh') no está instalado en Termux.")
        print("👉 Ejecuta primero: pkg install gh && gh auth login")
    except subprocess.CalledProcessError as e:
        print(f"❌ [ERROR] Falló la creación del Issue.\nDetalles: {e.stderr}")

if __name__ == "__main__":
    if len(sys.argv) >= 5:
        inyectar_experimento_gh(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        inyectar_experimento_gh(
            id_exp="EXP-002-A",
            variable="Gancho visual de alta retención (Primeros 2 segundos)",
            plataforma="YouTube Shorts & Reels",
            hipotesis="Al eliminar intros lentas e incorporar subtítulos dinámicos de alto contraste en los primeros 120 fotogramas, la retención en T+1h superará el 80%. Esto forzará al algoritmo a distribuir el contenido en canales orgánicos más amplios (no seguidores) durante la ventana T+24h."
        )
