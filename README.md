''' Simular una máquina de Galton con 3000 canicas y 12 niveles de obstáculos en Python, 
podemos usar la biblioteca matplotlib para graficar el histograma 
y la biblioteca random para simular el movimiento de las canicas.'''

import random
import matplotlib.pyplot as plt

def simular_canicas(num_canicas, num_niveles):
    '''Esta función simula la caída de num_canicas canicas a través de num_niveles de obstáculos.
    '''
    resultados = []
    for _ in range(num_canicas):
        posicion = 0
        for _ in range(num_niveles):
            paso = random.choice([-1, 1])  # -1 para izquierda, 1 para derecha
            posicion += paso
        resultados.append(posicion)
    return resultados

# Cada canica tiene la opción de moverse a la izquierda o a la derecha en cada nivel, 
# Representado por -1 y 1 respectivamente.
# La posición final de la canica se almacena en la lista resultados.

def graficar_histograma(resultados, num_niveles):
    '''Esta función toma los resultados de la simulación y crea un histograma usando matplotlib.
    '''
    plt.hist(resultados, bins=range(-num_niveles, num_niveles+2), edgecolor='black')
    plt.title('Simulación de Máquina de Galton')
    plt.xlabel('Posición final')
    plt.ylabel('Número de canicas')
    plt.grid(True)
    plt.show()
    
# El histograma muestra la distribución de las posiciones finales de las canicas.
# Los ejes están etiquetados y el gráfico tiene un título.
# Parámetros de la simulación

num_canicas = 3000
num_niveles = 12

# Realizamos la simulación y graficamos el resultado
resultados = simular_canicas(num_canicas, num_niveles)
graficar_histograma(resultados, num_niveles)
