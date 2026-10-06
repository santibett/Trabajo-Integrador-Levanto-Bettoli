import json
import os
from pathlib import Path
#dato = "app_web/salidas/mediciones-20260930-204656.json"
def cargar_json(dato):
    archivo_json = Path.cwd() / dato
    if not os.path.exists(archivo_json):
        print("El archivo json no existe")
        exit()
    with open(dato, "r") as archivo:
        datos = json.load(archivo)
    return (datos["registros_validos"])

def filtrar_datos(datos, estacion, medicion):
    lista_medicion = []
    for dato in datos:
        if dato["estacion_meteorologica"] == estacion:
            lista_medicion.append(dato[medicion])
    return lista_medicion
#print(filtrar_datos(cargar_json(dato),"AEROPARQUE AERO","temperatura"))
