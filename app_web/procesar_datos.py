import sys

from datos import cargar_json, filtrar_datos
from estadisticas import calcular_estadisticas
from graficos import generar_grafica


def main():
    ruta_json = sys.argv[1]
    estacion = sys.argv[2]
    medicion = sys.argv[3]

    datos = cargar_json(ruta_json) #Guarda el JSON completo
    filtrados = filtrar_datos(datos, estacion, medicion) #Devuelve una lista con las mediciones de la estacion
    estadisticas = calcular_estadisticas(filtrados)
    ruta_grafica = generar_grafica(filtrados, estacion, medicion)

    print(estadisticas)
    print(f"Grafica guardada en: {ruta_grafica}")


main()