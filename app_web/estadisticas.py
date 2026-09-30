def calcular_estadisticas(filtrados):
    maximo = filtrados[0]
    minimo = filtrados[0]
    suma=0
    canti_datos=len(filtrados)
    for dato in filtrados:
        if dato > maximo:
            maximo=dato
        if dato < minimo:
            minimo=dato
        suma += dato
    promedio=suma/canti_datos
    estadisticas={
        "Cantidad":canti_datos,
        "Minimo":minimo,
        "Maximo":maximo,
        "Promedio":promedio
    }
    return(estadisticas)

