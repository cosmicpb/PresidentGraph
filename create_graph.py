from cProfile import label
from grapheme import length
import numpy as np
import matplotlib.pyplot as plt
import csv

##CRIANDO ARRAY 1: ALEATÓRIA E ORDENADA DE 1000 ÍNDICES
cand1 = np.random.uniform(low=40.0, high=55.0, size=(1000,))
cand1[::-1].sort()

print('AVERAGE: ' + str(np.average(cand1)))

##CRIANDO ARRAY 3: 2000 PONTOS, VAZIA
cand1T = np.empty(2000)

##ADICIONANDO ARRAY 1 PARA ÍNDICES PARES DA ARRAY 3
cont = 0
for line in cand1:
    cand1T[cont*2] = float(line)
    cont = cont + 1


##CRIANDO ARRAY 2: ALEATÓRIA DE 1000 ÍNDICES
cand1D = np.random.uniform(low=40.0, high=60.0, size=(1000,))


#ADICIONANDO ARRAY 2 PARA ÍNDICES ÍMPARES DA ARRAY 3
cont = 0
for line in cand1D:
    cand1T[cont*2-1] = float(line)
    cont = cont + 1

#CRIANDO ARRAY PARA SOMA AGREGADA
cand1S = np.zeros(2001)

# FAZENDO A SOMA AGREGADA
cont2 = 0
for line in cand1T:
    
    cand1S[cont2+1] = cand1S[cont2] + cand1T[cont2]   
    cont2 = cont2 + 1


## CRIANDO ARRAY PARA MÉDIA AGREGADA
candcand1 = np.empty(2001)


cont = 0
for line in cand1S:
    candcand1[cont] = cand1S[cont]/(cont+1)
    cont = cont + 1


candFinal = np.empty(2000)
cont = 0
for line in candFinal:
    candFinal[cont] = candcand1[cont+1]
    cont = cont + 1

    


x = np.arange(0, 2000)




forca = np.empty(2000)
cont = 1
for line in forca:
    forca[cont-1] = 100/cont
    cont = cont + 1

cand2Final = np.zeros(2000)
it = 0
for line in candFinal:
    cand2Final[it] = 100 - candFinal[it]
    it = it + 1



fig, ax = plt.subplots()
ax.plot(x, candFinal, color='blue', label='Candidato 1')
ax.plot(x, cand2Final, color='red', label='Candidato 2')
ax.legend(bbox_to_anchor=(1, 0.9))
ax.set_xlabel('Evolução da contagem')
ax.set_ylabel('% de votos')

# ax.set_xlim(80, 2000)
# ax.set_ylim(0, 100)


# ax2 = ax.twinx()
# ax2.plot(x, forca, color='black', label='Força do voto')
# ax2.set_ylabel('Força de voto')
# ax2.legend()
plt.show()

