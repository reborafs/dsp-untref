# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def desvio_estandar(x):
    N = len(x)
    u = (1/N)*(np.sum(x))
    tau = np.sqrt((1/(N-1))*(np.sum(abs((x-u)**2))))
    return tau 

# =============================================================================
#               SENALES DEL EJERCICIO 1
# =============================================================================

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


# GENERACION DE RUIDO
ruido01 = np.random.normal(loc = 0, scale = 0.1, size = fs*t)
ruido1 = np.random.normal(loc = 0, scale = 1, size = fs*t)
ruido3 = np.random.normal(loc = 0, scale = 3, size = fs*t)

x01 = x + ruido01
x1 = x + ruido1
x3 = x + ruido3


# NORMALIZACION DE SENAL + RUIDO
Nx01 = x01/max(abs(x01))
Nx1 = x1/max(abs(x1))
Nx3 = x3/max(abs(x3))


# =============================================================================
#                              PLOTEO
# =============================================================================

fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
axs[0, 0].plot(vector_t, x)
axs[0, 0].set_title(r'$x(t)$')
axs[0, 1].plot(vector_t, Nx01, color='orange')
axs[0, 1].set_title('$x_{0.1}(t)$')
axs[1, 0].plot(vector_t, Nx1, color='green')
axs[1, 0].set_title('$x_1(t)$')
axs[1, 1].plot(vector_t, Nx3, color='black')
axs[1, 1].set_title('$x_3(t)$')
fig.tight_layout()

for ax in axs.flat:
    ax.set(xlabel='Tiempo [s]', ylabel='Amplitud')
    ax.grid()
    
plt.show()


# =============================================================================
#                       
# =============================================================================

SNR_x01= max(x01/desvio_estandar(ruido01))
SNR_x1= max(x1/desvio_estandar(ruido1))
SNR_x3= max(x3/desvio_estandar(ruido3))

print('''\n El SNR para la señal x01 es ''' , SNR_x01)
print('''\n El SNR para la señal x1 es ''' , SNR_x1)
print('''\n El SNR para la señal x3 es ''' , SNR_x3)

#Analizo lo mismo pero sin la componente de continua
xm =  x_2 + x_3

x01m = xm + ruido01
x1m = xm + ruido1
x3m = xm + ruido3

SNR_x01m = max(x01m/desvio_estandar(ruido01))
SNR_x1m = max(x1m/desvio_estandar(ruido1))
SNR_x3m = max(x3m/desvio_estandar(ruido3))

print('''\n El SNR para la señal x01 sin  la componente de continua es ''' , SNR_x01m)
print('''\n El SNR para la señal x1 sin  la componente de continua es ''' , SNR_x1m)
print('''\n El SNR para la señal x3  sin  la componente de continua es ''' , SNR_x3m)


#Analizo lo mismo pero aumentando el valor de la componente de continua
x_con = 10*np.ones_like(vector_t)
xn = x_con+ x_2 + x_3

x01n = xn + ruido01
x1n = xn + ruido1
x3n = xn + ruido3

SNR_x01n= max(x01n/desvio_estandar(ruido01))
SNR_x1n= max(x1n/desvio_estandar(ruido1))
SNR_x3n= max(x3n/desvio_estandar(ruido3))

print('''\n El SNR para la señal x01 aumentando la componente de continua de amplitud 10 es ''' , SNR_x01n)
print('''\n El SNR para la señal x1 aumentando la componente de continua de amplitud 10 es ''' , SNR_x1n)
print('''\n El SNR para la señal x3  aumentando la componente de continua de amplitud 10 es ''' , SNR_x3n)

print('''\n\n\n A modo de conclusión, a medida que aumenta la amplitud 
de la componente de constante continua, aumenta el valor de SNR.''')