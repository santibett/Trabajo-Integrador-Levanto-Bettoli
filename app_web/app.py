import streamlit as st
import sys
import pandas as pd
from datos import cargar_json, filtrar_datos
from estadisticas import calcular_estadisticas
from graficos import generar_grafica
from generar_csv import csv

def aplicacion():   
    st.title("App de Los Tiburones")
    if len(sys.argv) < 2:
        st.error("Error: Debe haber un JSON en la ruta")
        st.info("Ejemplo: streamlit run app_web/app.py -- tu_archivo.json")
        st.stop()
    ruta_json = sys.argv[1]
    datos = cargar_json(ruta_json)
    estaciones = []
    mediciones = ["Hora", "Temperatura", "Humedad", "Presion", "Direccion","Velocidad"]
    for i in datos:
        if i["estacion_meteorologica"] not in estaciones:
            estaciones.append(i["estacion_meteorologica"]) 
    estacion = st.selectbox("Seleccione la estacion", estaciones)
    medicion = st.selectbox("Seleccione una medicion", mediciones).lower()

    filtrados = filtrar_datos(datos, estacion, medicion)
    estadisticas = calcular_estadisticas(filtrados)
    st.subheader(f"Estadísticas para {medicion} en {estacion}")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Cantidad de datos", estadisticas.get("cantidad", estadisticas["Cantidad"]))
    with col2:
        st.metric("Minimo", estadisticas.get("minimo", estadisticas["Minimo"]))
    with col3:
        st.metric("Maximo", estadisticas.get("maximo", estadisticas["Maximo"]))
    with col4:
        st.metric("Promedio", estadisticas.get("promedio", estadisticas["Promedio"]))

    df_filtrado = pd.DataFrame(filtrados, columns=[f"{medicion.capitalize()} en {estacion}"])
    st.dataframe(df_filtrado)

    if st.button("Mostrar la grafica"):
        ruta_grafica = generar_grafica(filtrados,medicion,ruta_json,estacion)
        st.image(ruta_grafica, caption=f"Grafica de {medicion}")
    if st.button("Crear CSV"):
        csv(filtrados,medicion,ruta_json,estacion)
        st.text(f"Ya está disponible tu CSV con la {medicion} de {estacion} en la carpeta de Salidas!")
    

aplicacion()