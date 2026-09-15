import sys, validaciones, json
from datetime import datetime
from pathlib import Path

rutas=sys.argv

if validaciones.input(rutas): #Comprobamos que el formato en el que recivimos los datos sea correcto
    print("Formato de entrada incorrecto por favor use: python adaptar_datos.py datos/observaciones.txt datos/observaciones.json")
    exit()

txt=rutas[1]

ruta_json=rutas[2]

carpeta_json = Path.cwd() / "datos" / ruta_json
if not carpeta_json.is_dir():
    print("El directorio {carpeta_json} no existe")
    exit()

if validaciones.rutatxt(txt):
    print("La ruta con las observaciones del SMN no existe")
    exit()

registros_validos = []
registros_invalidos = []
total_registros = 0

with open(txt,"r") as observaciones:
    next(observaciones) #Saltamos el encabezado
    next(observaciones)
    for medicion in observaciones:
        mediciones=medicion.split()
        for i in range(len(mediciones)):    
            if mediciones[i].isalpha():
                mediciones[i]=" ".join(mediciones[i:])
                mediciones=mediciones[:i+1]
                break    #Permitimos nombres de lugares con mas de una palabra
        if len(mediciones)==0:
            continue
        if not mediciones[0].isdigit():
            continue #soluciona "R AERO", "�A AERO" y "O"
        total_registros += 1
        linea_original = "|".join(mediciones)
        #print(mediciones)
        if validaciones.cantidad_datos(mediciones):
            registros_invalidos.append({"linea_original": linea_original, "motivo_error": "Faltan o sobran datos"})
            continue
        if validaciones.fecha(mediciones[0]):
            registros_invalidos.append({"linea_original": linea_original, "motivo_error": f"Fecha incorrecta ({mediciones[0]})"})
            continue
        if validaciones.hora(mediciones[1]):
            registros_invalidos.append({"linea_original": linea_original, "motivo_error": f"Hora incorrecta ({mediciones[1]})"})
            continue
        if validaciones.temperatura(mediciones[2]):
            registros_invalidos.append({"linea_original": linea_original, "motivo_error": f"Temperatura incorrecta ({mediciones[2]})"})
            continue
        if validaciones.numeros(mediciones[2:7]):
            registros_invalidos.append({"linea_original": linea_original, "motivo_error": "Algunos parametros no son numeros"})
            continue
        if validaciones.humedad(mediciones[3]):
            registros_invalidos.append({"linea_original": linea_original, "motivo_error": f"Humedad fuera de rango ({mediciones[3]}%)"})
            continue
        if validaciones.presion(mediciones[4]):
            registros_invalidos.append({"linea_original": linea_original, "motivo_error": f"Presion incorrecta ({mediciones[4]})"})
            continue
        if validaciones.direccion(mediciones[5]):
            registros_invalidos.append({"linea_original": linea_original, "motivo_error": f"Direccion fuera de rango ({mediciones[5]})"})
            continue
        if validaciones.velocidad(mediciones[6]):
            registros_invalidos.append({"linea_original": linea_original, "motivo_error": f"Velocidad fuera de rango ({mediciones[6]})"})
            continue
        try:
            registro = {
                "estacion_meteorologica": mediciones[7],
                "anio": int(mediciones[0][4:]),
                "mes": int(mediciones[0][2:4]),
                "dia": int(mediciones[0][:2]),
                "hora": int(mediciones[1]),
                "temperatura": float(mediciones[2]),
                "humedad": int(float(mediciones[3])),
                "presion": float(mediciones[4]),
                "direccion": int(float(mediciones[5])),
                "velocidad": int(float(mediciones[6]))
            }
            registros_validos.append(registro)
        except Exception:
            registros_invalidos.append({"linea_original": linea_original, "motivo_error": "Error de conversión de tipos"})
        
salida_json = {
    "metadatos": {
        "total_registros": total_registros,
        "validos": len(registros_validos),
        "invalidos": len(registros_invalidos)
    },
    "registros_validos": registros_validos,
    "registros_invalidos": registros_invalidos
}

hora_actual = datetime.now()

formato =  "mediciones-" + hora_actual.strftime("%Y%m%d-%H%M%S") + ".json"

json_actual = carpeta_json / formato

with open(json_actual, "w") as archivo_json:
    json.dump(salida_json, archivo_json, indent=2)

print(f"Archivo json generado en {ruta_json}, cantidad de lineas leidas: {total_registros}, registros validos: {len(registros_validos)}")