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
    try:
        dia = int(num[:2])
        mes = int(num[2:4])
        anio = int(num[4:])
    except ValueError: 
        return True
    if 0>dia or dia>31 or 0>mes or mes>12:
        return True
    return False

def hora(num):
    try:
        num=int(num)
    except ValueError:
        return True
    if 0>num or num>23:
        return True
    return False
def temperatura(num):
    try:
        num = float(num)
    except ValueError: 
        return True
    if num > 50.0 or num < -40.0:
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
    try:
        num = float(num)
    except ValueError:
        return True
    if not 0.0<=num or num<=100.0:
        return True
    return False
def presion(num):
    try: 
        num = float(num)
    except ValueError:
        return True
    if num <= 870.0 or num >= 1084.0:
        return True
    return False
def direccion(num):
    try:
        num = float(num)
    except ValueError:
        return True
    if not 0.0<=num or num<=360.0:
        return True
    return False

def velocidad(num):
    try:
        num = float(num)
    except ValueError:
        return True
    if not 0.0<=num:
        return True
    return False