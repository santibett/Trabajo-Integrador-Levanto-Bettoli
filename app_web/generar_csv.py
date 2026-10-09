def csv(lista,medicion,ruta_json,estacion):
    encabezado=[]
    encabezado.append(medicion)
    ruta_json=ruta_json[21:-5]
    for i in lista:
        encabezado.append(str(i))
    with open ("app_web/salidas/csv/"+ruta_json+"_"+estacion+"_"+medicion+".csv","w") as archivo:
        for fila in encabezado:
            archivo.write(fila+"\n")
    return 1