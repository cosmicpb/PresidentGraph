from cProfile import label
from grapheme import length
import numpy as np
import matplotlib.pyplot as plt
import csv

##CREATING SORTED RANDOM ARRAY
cand1 = np.random.uniform(low=40.0, high=55.0, size=(1000,))
cand2 = np.zeros(1000)



cand1[::-1].sort()
it = 0
for line in cand1:
    cand2[it] = 100 - cand1[it]
    it = it + 1

print('CAND1:')
print(cand1)
print('CAND2:')
print(cand2)

print('Média Cand1:  ' + str(np.average(cand1)))
print('Média Cand2:  ' + str(np.average(cand2)))

##MOVING TO EVEN INDEXES
cand1T = np.zeros(2000)

cont = 0
for line in cand1:
    cand1T[cont*2] = float(line)
    cont = cont + 1

cand2T = np.zeros(2000)

cont = 0
for line in cand2:

    cand2T[cont*2] = float(line)
    cont = cont + 1

##CREATING UNIFORM RANDOM ARRAY
cand1D = np.random.uniform(low=40.0, high=60.0, size=(1000,))
cand2D = np.random.uniform(low=40.0, high=60.0, size=(1000,))

#MOVING TO ODD INDEXES
cont = 0
for line in cand1D:
    cand1T[cont*2-1] = float(line)
    cont = cont + 1

cont = 0
for line in cand2D:

    cand2T[cont*2-1] = float(line)
    cont = cont + 1


cand1S = np.zeros(2002)


cont2 = 0
for line in cand1T:
    cand1S[cont2+1] = cand1S[cont2] + line
    cont2 = cont2 + 1
print(cand1S)

candcand1 = np.zeros(2002)
cont = 0
for line in cand1S:
    candcand1[cont] = line/(cont+1)
    cont = cont + 1

candFinal = np.zeros(2000)
cont = 0
for line in candFinal:
    candFinal[cont] = candcand1[cont+1]
    cont = cont + 1

    
print(candFinal)

#CREATING AGGREGATE AVERAGE ARRAY
cand2S = np.zeros(2002)
cont2 = 0
for line in cand2T:
    cand2S[cont2+1] = cand2S[cont2] + line
    cont2 = cont2 + 1
print(cand2S)

cand2cand1 = np.zeros(2002)
cont = 0
for line in cand2S:
    cand2cand1[cont] = line/(cont+1)
    cont = cont + 1

cand2Final = np.zeros(2000)
cont = 0
for line in cand2Final:
    cand2Final[cont] = cand2cand1[cont+1]
    cont = cont + 1


x = np.arange(0, 2000)
print(x[1999])

plt.plot(x, candFinal, color='blue', label='Candidato 1')
plt.plot(x, cand2Final, color='red', label='Candidato 2')
plt.xlim([80,2000])
plt.legend()
plt.show()
