# Simple Numerical Laplace Equation Solution using MCM
import random, math
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from math import sqrt


# Dimensiones de la malla y delta
lenX = lenY = 8
delta = 1

# Condiciones de frontera
Ttop = 100
Tbottom = 0
Tleft = 0
Tright = 0

#puntos dentro de la malla
n_inside = (lenX-2) * (lenY-2)

#numero de random walks
N = 1000
#condicion cuando llega a la frontera
condit_front = True

# Color de deganeracion y color de la distribucion de la temperatura
colordegeneration = 100
colorMap = plt.cm.jet

# creacion de la malla
X, Y = np.meshgrid(np.arange(0, lenX), np.arange(0, lenY))

# Inicializar la malla
T = np.empty((lenX, lenY))
T.fill(-1) #para diferenciar los puntos conocidos de los que no se conocen

# Poniendo condiciones de frontera en la malla
T[:1, :] = Tbottom
T[:, (lenX-1):] = Tright
T[:, :1] = Tleft
T[(lenX-1):, :] = Ttop

#List storing data for convergence
conv_data = list()
conv_data_ctr = 0
conv_error = 1 / math.sqrt(N) #0.00000000001 #10^(-10)

def test_conv(prev_state, curr_state, lenX, lenY):
    sqrt_diff = 0
    for i in range(1, lenX-1, delta):
        for j in range(1, lenY-1, delta):
            sqrt_diff += pow(curr_state[i,j] - prev_state[i,j], 2)
    return sqrt(sqrt_diff)

def heat_transfer_MCM(lenX, lenY, delta, N, iteration, T):
    print('Por favor espere un momento... Sistema %d'%iteration)
    for i in range(1, lenX-1, delta):
        for j in range(1, lenY-1, delta):

            print "For point: ("+str(i)+","+str(j)+")"

            #rand_nrs = np.random.uniform(0, 1., N)

            T_w = list()
            #final_temp_point = 0
            for iter_walk in range(N):

                rand_nrs = np.random.uniform(0, 1., lenX*50)

                i_x = i
                j_x = j
                #rand_nr = rand_nrs[iter_walk]

                #condit_front = True
                rand_ctr = 0
                while 1:

                    #print rand_ctr
                    rand_nr = rand_nrs[rand_ctr]

                    #print "("+str(i_x)+","+str(j_x)+")"

                    #random_walk = random.uniform(0, 1., 3)
                    if 0 < rand_nr < 0.25:
                        i_x += 1
                        if i_x==(lenX-1): break

                    elif 0.25 < rand_nr < 0.5:
                        j_x += 1
                        if j_x==(lenY-1): break

                    elif 0.5 < rand_nr < 0.75:
                        i_x -= 1
                        if i_x==0: break

                    elif 0.75 < rand_nr < 1.:
                        j_x -= 1
                        if j_x==0: break

                    rand_ctr += 1

                T_w.append(T[j_x, i_x])
                #print "...appended."

            print "...done"
            T[j, i] = float(sum(T_w)) / float(len(T_w))

    print('... sistema %d completado'%iteration)
    return T

maxIter = 1
for iteration in range(0, maxIter):
    T_prev = deepcopy(T)
    T = heat_transfer_MCM(lenX, lenY, delta, N, iteration, T)
    conv_data.append(test_conv(T_prev, T, lenX, lenY))
    if conv_data_ctr>1:
        if abs(conv_data[conv_data_ctr]-conv_data[conv_data_ctr-1]) \
           < conv_error:
            print('(...desired convergence reached: '+str(conv_error)+'...)')
            print('At iteration: %d'%iteration)
            break
    conv_data_ctr += 1



plt.title('Temperatura distribuida')
plt.contourf(X, Y, T, colordegeneration, cmap=colorMap)
plt.colorbar()
plt.show()
