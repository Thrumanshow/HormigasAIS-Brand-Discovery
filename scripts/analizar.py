#!/usr/bin/env python3
import csv
import math
import os
import sys

def calcular_estadisticas(valores):
    if not valores:
        return 0.0, 0.0
    media = sum(valores) / len(valores)
    varianza = sum((x - media) ** 2 for x in valores) / len(valores)
    desviacion = math.sqrt(varianza)
    return media, desviacion

def analizar_experimentos():
    archivo_csv = "data/registro.csv"
    if not os.path.exists(archivo_csv) or os.stat(archivo_csv).st_size == 0:
        print("❌ [ANALIZADOR] No hay datos suficientes en data/registro.csv para procesar.")
        return

    exp_datos = {}

    with open(archivo_csv, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                id_exp = row["ID_Experimento"]
                ventana = row["Ventana"]
                vistas = float(row["Vistas_Organicas"])
                retencion = float(row["Retencion_Promedio"].replace("%", ""))
                interacciones = float(row["Interacciones"])

                if id_exp not in exp_datos:
                    exp_datos[id_exp] = []

                exp_datos[id_exp].append({
                    "ventana": ventana,
                    "vistas": vistas,
                    "retencion": retencion,
                    "interacciones": interacciones
                })
            except (KeyError, ValueError):
                continue

    print("\n=======================================================")
    print("🐜 HORMIGAS AIS - INFORME DE RENDIMIENTO DE ALGORITMO")
    print("=======================================================\n")

    for id_exp, lecturas in exp_datos.items():
        vistas_list = [l["vistas"] for l in lecturas]
        ret_list = [l["retencion"] for l in lecturas]
        
        media_vistas, σ_vistas = calcular_estadisticas(vistas_list)
        media_ret, σ_ret = calcular_estadisticas(ret_list)

        cv_vistas = (σ_vistas / media_vistas * 100) if media_vistas > 0 else 0.0

        print(f"📌 Experimento: {id_exp}")
        print(f"   • Lecturas registradas: {len(lecturas)}")
        print(f"   • Promedio Vistas: {media_vistas:.1f} (σ = ±{σ_vistas:.1f} | CV = {cv_vistas:.1f}%)")
        print(f"   • Promedio Retención: {media_ret:.1f}% (σ = ±{σ_ret:.1f}%)")

        if cv_vistas > 50:
            print("   🚀 [DIAGNÓSTICO] ALTA VOLATILIDAD: El algoritmo secundario ha entrado en fase de dispersión.")
        else:
            print("   ⚖️ [DIAGNÓSTICO] RENDIMIENTO ESTABLE: El alcance se mantiene dentro del baseline primario.")
        print("-" * 55)

if __name__ == "__main__":
    analizar_experimentos()
