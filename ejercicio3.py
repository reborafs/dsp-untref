# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 20:41:01 2021

@author: luna
"""
import numpy as np


n_i= [5, 10, 100, 1000, 10000, 100000]
tau_esperado: 1

tau_i= np.zeros(len(n_i))
porcentaje= np.zeros(len(n_i))
 
def desvio_estandar(x):
    N = len(x)
    u = (1/N)*(np.sum(x))
    tau = np.sqrt((1/(N-1))*(np.sum(abs((x-u)**2))))
    return tau 


for i in range (0, len(n_i)):
    for j in n_i:
        v= np.random.randn(0,n_i)
        tau_i[i]= desvio_estandar(v_)
        porcentaje[i]= tau_i[i]*100/tau_i
        j=j
        print('La señal con ' , str(j)' cantidad de muestras posee un desvío estandar del' ,porcentaje[i] '%.')