# Simple Numerical Laplace Equation Solution using Finite Difference Method
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from copy import deepcopy


#Function for testing convergence
def test_conv(prev_state, curr_state, lenX, lenY):
    sqrt_diff = 0
    for i in range(1, lenX-1, delta):
        for j in range(1, lenY-1, delta):
            sqrt_diff += pow(curr_state[i,j] - prev_state[i,j], 2)
    return sqrt(sqrt_diff)


if __name__=='__main__':

    # Iteracion del sistema
    maxIter = 200

    # Dimensiones de la malla y delta
    lenX = lenY = 8
    delta = 1

    # Condiciones de frontera
    Ttop = 100
    Tbottom = 0
    Tleft = 0
    Tright = 0

    # Supuesta temperatura dentro de la malla
    Tguess = 10

    # Color de deganeracion y color de la distribucion de la temperatura
    colordegeneration = 100
    colorMap = plt.cm.jet

    # creacion de la malla
    X, Y = np.meshgrid(np.arange(0, lenX), np.arange(0, lenY))

    # Inicializar la malla
    T = np.empty((lenX, lenY))
    T.fill(Tguess)

    # Poniendo condiciones de frontera en la malla
    T[:1, :] = Tbottom
    T[:, (lenX-1):] = Tright
    T[:, :1] = Tleft
    T[(lenX-1):, :] = Ttop

    #List storing data for convergence
    conv_data = list()
    conv_data_ctr = 0
    conv_error = 0.00000000001 #10^(-10)

    # Iteration (Se asume una estabilidad en maxIter = 500)
    print('Por favor espere un momento...')
    for iteration in range(0, maxIter):
        T_prev = deepcopy(T)
        for i in range(1, lenX-1, delta):
            for j in range(1, lenY-1, delta):
                T[i, j] = 0.25 * (T[i+1][j] + T[i-1][j] + T[i][j+1] + \
                          T[i][j-1])
        conv_data.append(test_conv(T_prev, T, lenX, lenY))
        if conv_data_ctr>1:
            if abs(conv_data[conv_data_ctr]-conv_data[conv_data_ctr-1]) \
               < conv_error:
                print('(...desired convergence reached: '+str(conv_error)+'...)')
                print('At iteration: %d'%iteration)
                break
        conv_data_ctr += 1

    print('...completado')

    plt.title('Temperatura distribuida')
    plt.contourf(X, Y, T, colordegeneration, cmap=colorMap)
    plt.colorbar()
    plt.show()
