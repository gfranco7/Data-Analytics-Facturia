import funciones
import pandas as pd
import os
from sqlalchemy import create_engine

engine = create_engine("sqlite:///facturas.db")

# 🔍 Cargar archivos ya procesados
try:
    archivos_existentes = pd.read_sql(
        "SELECT archivo FROM facturas", engine
    )["archivo"].tolist()
except:
    archivos_existentes = []

lista_df = []

# Recorrer carpetas
for carpeta in sorted(os.listdir("./facturas")):
    ruta_carpeta = os.path.join("./facturas/", carpeta)

    if not os.path.isdir(ruta_carpeta):
        continue

    for archivo in os.listdir(ruta_carpeta):

        if not archivo.lower().endswith(".pdf"):
            continue

        ruta_pdf = os.path.join(ruta_carpeta, archivo)

        # 🔥 VALIDACIÓN DUPLICADOS
        if ruta_pdf in archivos_existentes:
            print(f"⏭ Ya existe: {ruta_pdf}")
            continue

        print(f"📄 Procesando: {ruta_pdf}")

        try:
            texto = funciones.extraer_texto_pdf(ruta_pdf)
            csv = funciones.estructurar_texto(texto)

            if csv.strip().lower() == "error":
                print(f"❌ Error IA: {ruta_pdf}")
                continue

            df_factura = funciones.csv_a_dataframe(csv)

            # 🔥 guardar identificador único
            df_factura["archivo"] = ruta_pdf
            df_factura["moneda"] = "cop"

            lista_df.append(df_factura)

        except Exception as e:
            print(f"❌ Error procesando {ruta_pdf}: {e}")
            continue

# 🔥 concatenar una sola vez
if lista_df:
    df = pd.concat(lista_df, ignore_index=True)

    # limpiar columnas
    df = df[["fecha_factura", "proveedor", "concepto", "importe", "moneda", "archivo"]]

    # evitar duplicados internos
    df = df.drop_duplicates()

    # guardar en DB
    df.to_sql("facturas", engine, if_exists="append", index=False)
    
    print("✅ Proceso completado. Datos guardados en facturas.db")

else:
    print("⚠️ No se encontraron nuevas facturas para procesar.")
engine.dispose()
