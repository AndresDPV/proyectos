

import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import matplotlib as plt
import matplotlib.pyplot as plt
import random 
import operator
from mpl_toolkits.mplot3d import Axes3D
import numpy as np




"""# Listas de entrada a la red """

num=50                                                    # numero total de elementos de las listas   

temperatura=[0]*num                                       # se crea el vector vacio con 30 elementos "temperatura"
for i in range (num):
  temperatura[i]=random.randint(1,30)                     # se asignan valores al azar entre [1,25]


altura=[0]*num                                            # se crea el vector vacion con 30 elementos "altura"
for i in range (num):
  altura[i]=random.randint(1,20)                          # se asignan valores al azar entre [1,10]





"""# Pesos y bias """

pesos1=[0]*num
pesos2=[0]*num

for i in range(num):
  pesos1[i]=0.15         # peso #1
  pesos2[i]=-0.4         # peso #2


bias=[0]*num             # creacion para la lista llamada " bias "

for i in range(num):
  bias[i]=0.1





"""# Funcion de activacion """

a=[0]*num
b=[0]*num
c=[0]*num

for i in range(num):
  a[i]=pesos1[i]*temperatura[i]
  b[i]=pesos2[i]*altura[i]
  c[i]=a[i]+b[i]+bias[i]              # Red neuronal en 2D




"""#decisión  (aprobado no aprobado)"""

#for i in range(num):  
  #if c[i] > 0:                       # condicional necesario para realizar la clasificación
     # print("aceptado")
  #else:
     # print("no aceptado")






"""# gráfica """

def f(x):
  return 0.5*x                         # función lineal 

x= list(range(1,51))                   # variable independoente de la función lineal 
y=[f(i) for i in (x)]                  # f(x)



# listas necesarias para realizar la clasifiacion en el gráfico 

altura2=[]
temperatura2=[]
altura3=[]
temperatura3=[]




for i in range (num):
  for element in x:
    if element==temperatura[i]:
      if altura[i]>((element/2)):        # condicional comparativo para realizar la clasificacion por encima o debajo de la fución lineal 
        altura2.append(altura[i])
        temperatura2.append(temperatura[i])
      else:
        altura3.append(altura[i])
        temperatura3.append(temperatura[i])

print(altura2)
print(temperatura2)



fig,ax = plt.subplots(1)
plt.plot(temperatura2,altura2,'o')
plt.plot(temperatura3,altura3,'o')
ax.plot(y)
plt.show()




"""# NEURONAL NETWORK 3D """

pesos3=[0]*num


for i in range(num):
  pesos3[i]=-0.1                          # peso para la tercer entrada



funcion4=[0]*num
velocidad=[0]*num
for i in range (num):
  velocidad[i]=random.randint(1,38)           # variable de entrada de la red #3





"** frontera de decisión**"

# for i in range(n):
#  if funcion4[i] > 0:
#   print("aceptado")
#  else:
#    print("no aceptado")




"** gráfico**"


X, Y = np.meshgrid(np.linspace(-20, 20, 100), np.linspace(-20, 20, 100))

Z=(-14*X +(3*Y-70))+10


fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
ax.scatter(temperatura,altura,velocidad,marker='o',color='tab:red')

X, Y = np.meshgrid(np.linspace(-20, 20, 100), np.linspace(-20, 20, 100))

Z=(-14*X +(3*Y-70))+10


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()