# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 10:54:12 2021

@author: luna
"""
import numpy as np
from matplotlib import pyplot as plt

def h_convo(x, M):
    escalon = np.concatenate((np.ones(M),np.zeros(len(x)-M+1)))
    
    y = np.zeros(len(x)-M+1)
   
    for i in range(len(x)-M+1):
        
        y = (np.convolve(x,escalon))/M

    return y

t = np.linspace(0,3,3*10)
x = 0.5*np.sin(2*np.pi*500*t)
ruido = np.random.normal(0,1,3*10)
xr =  x + ruido

y = h_convo(xr, 10)

fig, axs= plt.subplots(2,1, constrained_layout=True)
axs[0].plot(t, xr) 
axs[0].grid(True)
axs[0].set_xlabel('tiempo [s]')
axs[0].set_ylabel('amplitud')
axs[0].set_title('Señal original con ruido')
axs[1].plot(t, y)
axs[1].set_title('Señal filtrada')
axs[1].grid(True)
plt.show ()

