import streamlit as st
import sys
from datos import cargar_json, filtrar_datos
from estadisticas import calcular_estadisticas
from graficos import generar_grafica
from csv import csv

def aplicacion():
    ruta_json = sys.argv[1]

    estacion = st.selectbox