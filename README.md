# Trabajo-Integrador-Levanto-Bettoli

## Integrantes
[Santiago Bettoli]
[Juan Cruz Levanto]

## Descripción
Este proyecto es un conversor de datos meteorológicos desarrollado en Python. Lee archivos de texto plano (`.txt`) provistos por el Servicio Meteorológico Nacional (SMN), valida y procesa las observaciones, y genera un archivo `.json` estructurado para su posterior consumo en aplicaciones web.

## Requisitos
Python 3.x instalado. No se requieren librerías externas (solo módulos nativos de Python).

## Instrucciones de Ejecución
El script `adaptar_datos.py` se ejecuta desde la consola pasando la ruta del archivo `.txt` de entrada y la ruta donde se guardará el `.json` de salida.

```bash
python adaptar_datos.py datos/observaciones.txt datos/observaciones.json
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