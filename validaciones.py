import os

def rutatxt(ruta):
    return not os.path.exists(ruta)

def input(rutas):
    if len(rutas) != 3 or ".txt" not in rutas[1] or ".json" not in rutas[2]:
        return True
    return False

def cantidad_datos(mediciones):
    if len(mediciones) != 8:
        return True
    return False

def fecha (num):
    if len(num)!=8:
        return True
    if not num.isnumeric():
        return True
    
    dia = int(num[:2])
    mes = int(num[2:4])
    anio = int(num[4:])
    if 0>dia>31 or 0>mes>12:
        return True
    return False

def hora(num):
    if not num.isnumeric():
        return True
    num=int(num)
    if 0>num>23:
        return True
    return False

def numeros(valores):
    for numero in valores:
        # Quitamos el '-' inicial y el primer '.' antes de evaluar .isdigit()
        es_num = numero.lstrip("-").replace(".", "").isdigit()
        if not es_num:
            return True         
    return False

def humedad(num):
    num = int(num)
    if not 0<=num<=100:
        return True
    return False

def direccion(num):
    num = int(num)
    if not 0<=num<=360:
        return True
    return False

def velocidad(num):
    num = int(num)
    if not 0<=num:
        return True
    return False