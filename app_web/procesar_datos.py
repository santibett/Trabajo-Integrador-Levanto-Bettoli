import sys

from datos import cargar_json, filtrar_datos
from estadisticas import calcular_estadisticas
from graficos import generar_grafica
from csv import csv

def main():
    ruta_json = sys.argv[1]
    estacion = sys.argv[2]
    medicion = sys.argv[3]

    datos = cargar_json(ruta_json) #Guarda el JSON completo
    filtrados = filtrar_datos(datos, estacion, medicion) #Devuelve una lista con las mediciones de la estacion
    estadisticas = calcular_estadisticas(filtrados)
    ruta_grafica = generar_grafica(filtrados,medicion,ruta_json,estacion)
    csv(filtrados,medicion,ruta_json,estacion)

    print("Estadisticas:")
    print(f"\tCantidad de {medicion}/s en {estacion}: {estadisticas["Cantidad"]}")
    print(f"\t{medicion.capitalize()} maxima: {estadisticas["Maximo"]}")
    print(f"\t{medicion.capitalize()} minima: {estadisticas["Minimo"]}")
    print(f"\t{medicion.capitalize()} promedio: {estadisticas["Promedio"]}")
    print("5 primeros datos:")
    for i in range (5):
        print("\t",filtrados[i])
    print(f"Grafica guardada en: {ruta_grafica}")


main()