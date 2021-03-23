# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 23:00:02 2021

@author: luna
"""
import numpy as np
import matplotlib.pyplot as plt

def desvio_estandar(x):
    N = len(x)
    u = (1/N)*(np.sum(x))
    tau = np.sqrt((1/(N-1))*(np.sum(abs((x-u)**2))))
    return tau 

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


x_1 = 2*np.ones_like(vector_t)
x_2 = np.cos(2*np.pi*f2*vector_t)*(np.e**(-exp2))
x_3 = np.sin(2*np.pi*f3*vector_t)*(np.e**(-exp3))


x = x_1 + x_2 + x_3

ruido01 = np.random.normal(loc = 0, scale = 0.1, size = fs*t)
ruido1 = np.random.normal(loc = 0, scale = 1, size = fs*t)
ruido3 = np.random.normal(loc = 0, scale = 3, size = fs*t)

x01 = x + ruido01
x1 = x + ruido1
x3 = x + ruido3


#vectores normalizados
Nx01 = x01/max(x01)
Nx1 = x1/max(x1)
Nx3 = x3/max(x3)

fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
axs[0, 0].plot(vector_t, x)
axs[0, 0].set_title('x(t)')
axs[0, 1].plot(vector_t, Nx01, color='orange')
axs[0, 1].set_title('(x01)(t)')
axs[1, 0].plot(vector_t, Nx1, color='green')
axs[1, 0].set_title('(x1)(t)')
axs[1, 1].plot(vector_t, Nx3, color='black')
axs[1, 1].set_title('(x3)(t)')
fig.tight_layout()

for ax in axs.flat:
    ax.set(xlabel='Tiempo [s]', ylabel='Amplitud')
    ax.grid()
    
plt.show()

SNR_x01= max(x01/desvio_estandar(ruido01))
SNR_x1= max(x1/desvio_estandar(ruido1))
SNR_x3= max(x3/desvio_estandar(ruido3))

print('''\n El SNR para la señal x01 es ''' , SNR_x01)
print('''\n El SNR para la señal x1 es ''' , SNR_x1)
print('''\n El SNR para la señal x3 es ''' , SNR_x3)




