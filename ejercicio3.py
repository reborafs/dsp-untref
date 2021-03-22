# -*- coding: utf-8 -*-

import numpy as np

def desvio_estandar(x):
    N = len(x)
    u = (1/N)*(np.sum(x))
    tau = np.sqrt((1/(N-1))*(np.sum(abs((x-u)**2))))
    return tau 

v1 = np.random.randn(5)
v2 = np.random.randn(10)
v3 = np.random.randn(100)
v4 = np.random.randn(1000)
v5 = np.random.randn(10000)
v6 = np.random.randn(100000)

d1 = desvio_estandar(v1)
d2 = desvio_estandar(v2)
d3 = desvio_estandar(v3)
d4 = desvio_estandar(v4)
d5 = desvio_estandar(v5)
d6 = desvio_estandar(v6)

p1 = d1*100
p2 = d2*100
p3 = d3*100
p4 = d4*100
p5 = d5*100
p6 = d6*100

print('''Para la cantidad de muestras N = 5:\n
      La desviacion estandar es:''', d1,
      '\n\tCon un porcentaje de: ', round(p1,2), '%\n')
print('''Para la cantidad de muestras N = 10:\n
      La desviacion estandar es:''', d2,
      '\n\tCon un porcentaje de: ', round(p2,2), '%\n')
print('''Para la cantidad de muestras N = 100:\n
      La desviacion estandar es:''', d3,
      '\n\tCon un porcentaje de: ', round(p3,2), '%\n')
print('''Para la cantidad de muestras N = 1000:\n
      La desviacion estandar es:''', d4,
      '\n\tCon un porcentaje de: ', round(p4,2), '%\n')
print('''Para la cantidad de muestras N = 10000:\n
      La desviacion estandar es:''', d5,
      '\n\tCon un porcentaje de: ', round(p5,2), '%\n')
print('''Para la cantidad de muestras N = 100000:\n
      La desviacion estandar es:''', d6,
      '\n\tCon un porcentaje de: ', round(p6,2), '%\n')