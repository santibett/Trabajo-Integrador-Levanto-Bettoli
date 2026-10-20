from estadisticas import calcular_estadisticas

entrada = [1,2,3,4,5]
salida={
    "Cantidad":5,
    "Minimo":1,
    "Maximo":5,
    "Promedio":3
}

def test_estadisticas_cantidad():
    assert calcular_estadisticas(entrada)["Cantidad"] == salida["Cantidad"]

def test_estadisticas_minimo():
    assert calcular_estadisticas(entrada)["Minimo"] == salida["Minimo"]

def test_estadisticas_maximo():
    assert calcular_estadisticas(entrada)["Maximo"] == salida["Maximo"]

def test_estadisticas_promedio():
    assert calcular_estadisticas(entrada)["Promedio"] == salida["Promedio"]