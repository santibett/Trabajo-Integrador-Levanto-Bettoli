import matplotlib.pyplot as plt

def generar_grafica(lista, medicion, ruta_json, estacion):
    ruta_json = ruta_json[21:-5]

    numeros = list(range(len(lista)))

    plt.figure(figsize=(10, 5))
    plt.plot(numeros, lista)
    plt.title(f"{medicion} - {estacion}")
    plt.xlabel("Medición")
    plt.ylabel(medicion)
    plt.grid(True)

    ruta = f"app_web/salidas/png/{ruta_json}_{estacion}_{medicion}.png"
    plt.savefig(ruta)
    plt.close()

    return ruta