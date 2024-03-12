def calcular_velocidad(distancia, tiempo):
    velocidad = distancia / tiempo
    return velocidad
def principal():
    distancia = float(input("Ingresa la distancia recorrida por el automóvil (en metros): "))
    tiempo = float(input("Ingresa el tiempo que tardó el automóvil en recorrer la distancia (en segundos): "))
    velocidad = calcular_velocidad(distancia, tiempo)
    print("La velocidad del automóvil es {:.2f} metros por segundo.".format(velocidad))

if __name__ == "__main__":
    principal()