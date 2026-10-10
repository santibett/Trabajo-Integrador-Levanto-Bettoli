# Trabajo-Integrador-Levanto-Bettoli

## Integrantes
* Santiago Bettoli
* Juan Cruz Levanto

## Descripción
Este proyecto es un conversor de datos meteorológicos desarrollado en Python. Lee archivos de texto plano (`.txt`) provistos por el Servicio Meteorológico Nacional (SMN), valida y procesa las observaciones, y genera un archivo `.json` estructurado para su posterior consumo en aplicaciones web.

## Requisitos
* Python 3.x instalado. No se requieren librerías externas (solo módulos nativos de Python).

## Instrucciones de Ejecución
El script `adaptar_datos.py` se ejecuta desde la consola pasando la ruta del archivo `.txt` de entrada y el directorio donde se guardará el `.json` de salida.

```bash
python conversor/adaptar_datos.py app_web/datos/observaciones.txt salidas
```

El archivo JSON resultante sigue esta estructura, dividiendo las observaciones entre válidas e inválidas, e incluyendo un resumen del procesamiento:
```json
{
  "metadatos": {
    "total_registros": 2,
    "validos": 1,
    "invalidos": 1
  },
  "registros_validos": [
    {
      "estacion_meteorologica": "BARILOCHE AERO",
      "anio": 2026,
      "mes": 8,
      "dia": 20,
      "hora": 10,
      "temperatura": 9.9,
      "humedad": 65,
      "presion": 1004.3,
      "direccion": 290,
      "velocidad": 28
    }
  ],
  "registros_invalidos": [
    {
      "linea_original": "20082026|10|15.0|150|1012.0|290|28|EZEIZA AERO",
      "motivo_error": "Humedad fuera de rango (150%)"
    }
  ]
}
```
---

## Segunda Parte: Análisis de datos y App Web

## Descripción
Esta segunda parte consiste en construir una aplicación para explorar los datos meteorológicos a partir del archivo JSON validado que fue generado en la primera parte. La solución se divide en dos etapas:

1. **Procesamiento de datos:** Un script que procesa los argumentos recibidos por la línea de comandos para cargar el JSON válido, filtrar los datos según la estación meteorológica y la medición seleccionadas, y calcular estadísticas básicas (cantidad, mínimo, máximo y promedio). Además, genera un CSV con la estación y las mediciones correspondientes, y exporta una gráfica en formato PNG usando Matplotlib.
2. **Aplicación Web:** Una interfaz desarrollada con Streamlit que reutiliza las funciones de la etapa anterior. Permite seleccionar la estación y la medición mediante controles interactivos, muestra las estadísticas calculadas, exhibe una tabla de los datos acomodada con Pandas y visualiza la gráfica generada.

## Requisitos
Para ejecutar esta segunda parte, es necesario instalar las librerías gráficas y de datos requeridas:

```bash
pip install matplotlib streamlit pandas
```

## Instrucciones de Ejecución

### Etapa 1: Procesamiento desde la consola
El programa principal `procesar_datos.py` recibe tres argumentos desde la consola:
1. La ruta del archivo JSON de entrada.
2. La estación meteorológica (con comillas).
3. La medición a analizar.

```bash
python app_web/procesar_datos.py app_web/salidas/json/mediciones-20260915-214155.json "AEROPARQUE AERO" temperatura
```

### Etapa 2: Aplicación Web con Streamlit
Para iniciar la aplicación web, se debe ejecutar `app.py` pasándole como argumento la ruta del archivo JSON.

```bash
streamlit run app_web/app.py -- app_web/salidas/json/mediciones-20260915-214155.json
```