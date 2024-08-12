import random
import matplotlib.pyplot as plt

def simular_canicas(num_canicas, num_niveles):
    resultados = []
    for _ in range(num_canicas):
        posicion = 0
        for _ in range(num_niveles):
            paso = random.choice([-1, 1])  # -1 para izquierda, 1 para derecha
            posicion += paso
        resultados.append(posicion)
    return resultados

def graficar_histograma(resultados, num_niveles):
    plt.hist(resultados, bins=range(-num_niveles, num_niveles+2), edgecolor='black')
    plt.title('Simulación de Máquina de Galton')
    plt.xlabel('Posición final')
    plt.ylabel('Número de canicas')
    plt.grid(True)
    plt.show()

# Parámetros de la simulación
num_canicas = 3000
num_niveles = 12

# Realizamos la simulación y graficamos el resultado
resultados = simular_canicas(num_canicas, num_niveles)
graficar_histograma(resultados, num_niveles)
