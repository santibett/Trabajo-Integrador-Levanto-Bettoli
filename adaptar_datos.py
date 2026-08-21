import sys, validaciones

rutas=sys.argv

if validaciones.input(rutas): #Comprobamos que el formato en el que recivimos los datos sea correcto
    print("Formato de entrada incorrecto por favor use: python adaptar_datos.py datos/observaciones.txt datos/observaciones.json")
    exit()

txt=rutas[1]

json=rutas[2]

if validaciones.rutatxt(txt):
    print("La ruta con las observaciones del SMN no existe")
    exit()

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
        print(mediciones)
        if validaciones.cantidad_datos(mediciones):
            # guardar que esta medicion no es correcta pq faltan datos (hacer)
            continue
        if validaciones.fecha(mediciones[0]):
            # guardar que esta medicion no es correcta pq el dia esta mal (hacer)
            continue
        if validaciones.hora(mediciones[1]):
            # guardar que esta medicion no es correcta pq la hora esta mal (hacer)
            continue
        if validaciones.numeros(mediciones[2:7]):
            # guardar que esta medicion no es correcta pq alguno no es numero (mejorable) (hacer)
            continue
        if validaciones.humedad(mediciones[3]):
            # guardar que esta medicion no es correcta pq la humedad esta fuera de rango (hacer)
            continue
        if validaciones.direccion(mediciones[5]):
            # guardar que esta medicion no es correcta pq la direccion esta fuera de rango (hacer)
            continue
        if validaciones.velocidad(mediciones[6]):
            # guardar que esta medicion no es correcta pq la velocidad esta fuera de rango (hacer)
            continue
        