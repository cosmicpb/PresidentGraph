from cProfile import label
from grapheme import length
import numpy as np
import matplotlib.pyplot as plt
import csv

##CREATING SORTED RANDOM ARRAY
bolso = np.random.uniform(low=40.0, high=55.0, size=(1000,))
lula = np.random.uniform(low=45.0, high=60.0, size=(1000,))

bolso[::-1].sort()
lula.sort()

##MOVING TO EVEN INDEXES
bolsoT = np.zeros(2000)

cont = 0
for line in bolso:
    bolsoT[cont*2] = float(line)
    cont = cont + 1

lulaT = np.zeros(2000)

cont = 0
for line in lula:

    lulaT[cont*2] = float(line)
    cont = cont + 1

##CREATING UNIFORM RANDOM ARRAY
bolsoD = np.random.uniform(low=40.0, high=60.0, size=(1000,))
lulaD = np.random.uniform(low=40.0, high=60.0, size=(1000,))

#MOVING TO ODD INDEXES
cont = 0
for line in bolsoD:
    bolsoT[cont*2-1] = float(line)
    cont = cont + 1

cont = 0
for line in lulaD:

    lulaT[cont*2-1] = float(line)
    cont = cont + 1


bolsoS = np.zeros(2002)


cont2 = 0
for line in bolsoT:
    bolsoS[cont2+1] = bolsoS[cont2] + line
    cont2 = cont2 + 1
print(bolsoS)

candBolso = np.zeros(2002)
cont = 0
for line in bolsoS:
    candBolso[cont] = line/(cont+1)
    cont = cont + 1

candFinal = np.zeros(2000)
cont = 0
for line in candFinal:
    candFinal[cont] = candBolso[cont+1]
    cont = cont + 1

    
print(candFinal)

#CREATING AGGREGATE AVERAGE ARRAY
lulaS = np.zeros(2002)
cont2 = 0
for line in lulaT:
    lulaS[cont2+1] = lulaS[cont2] + line
    cont2 = cont2 + 1
print(lulaS)

lulaBolso = np.zeros(2002)
cont = 0
for line in lulaS:
    lulaBolso[cont] = line/(cont+1)
    cont = cont + 1

lulaFinal = np.zeros(2000)
cont = 0
for line in lulaFinal:
    lulaFinal[cont] = lulaBolso[cont+1]
    cont = cont + 1


x = np.arange(0, 2000)
print(x[1999])

plt.plot(x, lulaFinal, color='red')
plt.plot(x, candFinal, color='blue')
plt.show()
