# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 15:51:23 2021

@author: luna
"""


import numpy as np

def valor_medio(x):
    N = len(x)
    u = np.dot((1/N), (np.sum(x, initial=0, where= N-1)))
    return u

def desvio_medio(x):
    N = len(x)
    u = np.dot((1/N), (np.sum(x, initial=0, where= N-1)))
    d = np.dot((1/N),(np.sum(np.absolute(x-u), initial= 0, where= N)))
    return d

def desvio_estandar(x):
    N = len(x)
    u = np.dot((1/N), (np.sum(x, initial=0, where= N-1)))
    tau = np.dot((1/N),(np.sum(np.absolute((x-u)**2), initial= 0, where= N)))
    return tau 

def rms(x):
    N = len(x)
    rms = np.sqrt(np.dot((1/N),(np.sum(np.absolute(x**2), initial= 0, where= N))))
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
sigma3 = 0.007
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