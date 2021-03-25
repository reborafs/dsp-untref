# -*- coding: utf-8 -*-

import numpy as np

def valor_medio(x):
    u = (1/len(x))*np.sum(x)
    return u

def desvio_medio(x):
    N = len(x)
    u = (1/N)*np.sum(x)
    d = (1/N)*np.sum(abs(x-u))
    return d

def desvio_estandar(x):
    N = len(x)
    u = (1/N)*(np.sum(x))
    tau = np.sqrt((1/(N-1))*(np.sum(abs((x-u)**2))))
    return tau 

def rms(x):
    N = len(x)
    rms = np.sqrt((1/N)*np.sum(abs(x**2)))
    return rms
    

t = 1
fs = 44100
vector_t = np.linspace(0,t,t*fs)

f2 = 10000
u2 = 0.2
sigma2 = 0.05
exp2 = ((vector_t-u2)**2)/(2*(sigma2**2))

f3 = 500
u3 = 0.7
sigma3 = 0.07
exp3 = ((vector_t-u3)**2)/(2*(sigma3**2))


x1 = 2*np.ones_like(vector_t)
x2 = np.cos(2*np.pi*f2*vector_t)*(np.e**(-exp2))
x3 = np.sin(2*np.pi*f3*vector_t)*(np.e**(-exp3))

valor1 = valor_medio(x1)
valor2 = valor_medio(x2)
valor3 = valor_medio(x3)

desvio_medio1 = desvio_medio(x1)
desvio_medio2 = desvio_medio(x2)
desvio_medio3 = desvio_medio(x3)

desvio_estandar1 = desvio_estandar(x1)
desvio_estandar2 = desvio_estandar(x2)
desvio_estandar3 = desvio_estandar(x3)

rms1 = rms(x1)
rms2 = rms(x2)
rms3 = rms(x3)


#============================================================================#
#                               NUMPY TEST
#============================================================================#

# valor1 = np.mean(x1)
# valor2 = np.mean(x2)
# valor3 = np.mean(x3)

#3 No se encuentra funcion equivalente en numpy.
# desvio_medio1 = desvio_medio(x1)
# desvio_medio2 = desvio_medio(x2)
# desvio_medio3 = desvio_medio(x3)

# desvio_estandar1 = np.std(x1)
# desvio_estandar2 = np.std(x2)
# desvio_estandar3 = np.std(x3)

# rms1 = np.sqrt(np.mean(x1**2))
# rms2 = np.sqrt(np.mean(x2**2))
# rms3 = np.sqrt(np.mean(x3**2))


print('''\nLos valores medios para las señales son: \n
     x1 = ''', valor1, '''\n
     x2 = ''', valor2, '''\n
     x3 = ''', valor3)
 
print('''\nLos desvios medios para las señales son: \n
     x1 = ''', desvio_medio1, '''\n
     x2 = ''', desvio_medio2, '''\n
     x3 = ''', desvio_medio3)
     
print('''\nLos desvios estandar para las señales son: \n
     x1 = ''', desvio_estandar1, '''\n
     x2 = ''', desvio_estandar2, '''\n
     x3 = ''', desvio_estandar3)
     
print('''\nLos valores RMS para las señales son: \n
     x1 = ''', rms1, '''\n
     x2 = ''', rms2, '''\n
     x3 = ''', rms3)