#!/usr/bin/env python3
import csv
import sys
import os

def main():
    archivo_csv = "data/registro.csv"
    if not os.path.exists(archivo_csv):
        print(f"❌ Error: {archivo_csv} no existe.")
        sys.exit(1)

    # Parsear argumentos dinámicos en formato clave=valor
    nuevos_datos = {}
    for arg in sys.argv[1:]:
        if "=" in arg:
            k, v = arg.split("=", 1)
            nuevos_datos[k.strip()] = v.strip() if v.strip() != "" else "unknown"

    # Leer encabezados del CSV existente
    with open(archivo_csv, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        encabezados = next(reader, None)

    if not encabezados:
        print("❌ Error: El archivo CSV está vacío o sin encabezados.")
        sys.exit(1)

    # Construir la nueva fila mapeando exactamente contra los encabezados del CSV
    nueva_fila = []
    for col in encabezados:
        nueva_fila.append(nuevos_datos.get(col, "unknown"))

    # Inyectar la fila al final del registro
    with open(archivo_csv, mode="a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(nueva_fila)

    print(f"✅ [REGISTRO SOBERANO] Fila inyectada imparcialmente en {archivo_csv}")

if __name__ == "__main__":
    main()
