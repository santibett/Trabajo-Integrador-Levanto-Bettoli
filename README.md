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
## Segunda Parte

## Descripcion
Esta segunda parte consiste en contruir una aplicacion a partir del JSON generado en la primer parte, con los datos especificos de estacion y medicion. 
El script procesa los argumentos recibidos por la linea de comandos para cargar el JSON valido, filtrar los datos segun la estacion meteorologica y la medicion seleccionadas, calcular las estadisticas basicas como maximo, minimo y promedio, generar un CSV con la estacion y debajo cada medicion, y por ultimo generar una grafica en dormato PNG usando Matplotlib.

## Requisitos
Tener instalada la libreria grafica ( pip install matplotlib )
codigo para venv: source .venv/bin/activate
instalar streamlit: pip install streamlit pandas
## Instrucciones de Ejecucion
El programa principal procesar_datos.py recibe tres argumentos desde la consola:
La ruta del archivo JSON de entrada.
La estación meteorológica (con comillas).
La medición a analizar.

```bash
python app_web/procesar_datos.py app_web/salidas/json/mediciones-20260915-214155.json "AEROPARQUE AERO" temperatura
```
```bash
streamlit run app_web/app.py -- app_web/salidas/json/mediciones-20260915-214155.json
```
