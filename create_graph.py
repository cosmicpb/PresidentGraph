from cProfile import label
from grapheme import length
import numpy as np
import matplotlib.pyplot as plt
import csv

##CREATING SORTED RANDOM ARRAY
cand1 = np.random.uniform(low=40.0, high=55.0, size=(1000,))




cand1[::-1].sort()

##MOVING TO EVEN INDEXES
cand1T = np.empty(2000)

cont = 0
for line in cand1:
    cand1T[cont*2] = float(line)
    cont = cont + 1



##CREATING UNIFORM RANDOM ARRAY
cand1D = np.random.uniform(low=40.0, high=60.0, size=(1000,))


#MOVING TO ODD INDEXES
cont = 0
for line in cand1D:
    cand1T[cont*2-1] = float(line)
    cont = cont + 1


cand1S = np.zeros(2002)

print(cand1S)
cont2 = 0
for line in cand1T:
    
    cand1S[cont2+1] = cand1S[cont2] + cand1T[cont2]   
    cont2 = cont2 + 1



candcand1 = np.empty(2002)
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
# print(x[1999])



forca = np.empty(2000)
cont = 1
for line in forca:
    forca[cont-1] = 100/cont
    cont = cont + 1
# print(forca)


# plt.plot()
# plt.xlim([80,2000])
# plt.ylim([0,100])
# 
# plt.show()

cand2Final = np.zeros(2000)
it = 0
for line in candFinal:
    cand2Final[it] = 100 - candFinal[it]
    it = it + 1

# print('CAND 1: ------------------------------------------------')
# print(candFinal)
# print('CAND 2: ------------------------------------------------')
# print(cand2Final)

fig, ax = plt.subplots()
ax.plot(x, candFinal, color='blue', label='Candidato 1')
ax.plot(x, cand2Final, color='red', label='Candidato 2')
ax.legend(bbox_to_anchor=(1, 0.9))
ax.set_xlabel('Evolução da contagem')
ax.set_ylabel('% de votos')

# ax.set_xlim(80, 2000)
# ax.set_ylim(0, 100)


ax2 = ax.twinx()
ax2.plot(x, forca, color='black', label='Força do voto')
ax2.set_ylabel('Força de voto')
ax2.legend()
plt.show()

