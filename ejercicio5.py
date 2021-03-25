# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
#                       SENALES DEL EJERCICIO 1
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
sigma3 = 0.07
exp3 = ((vector_t-u3)**2)/(2*(sigma3**2))


x_1 = 2*np.ones_like(vector_t)
x_2 = np.cos(2*np.pi*f2*vector_t)*(np.e**(-exp2))
x_3 = np.sin(2*np.pi*f3*vector_t)*(np.e**(-exp3))


signal = x_1 + x_2 + x_3

# =============================================================================
#                       GENERACION DE RUIDO
# =============================================================================


## EL PROMEDIO NO SABEMOS SI ESTA BIEN HECHO, HAY QUE USAR RMS OR WHAT?

total = np.zeros_like(vector_t)

for i in range (10):
    noise = np.random.normal(0, 3, len(vector_t))
    signal_with_noise = signal + noise
    total += signal_with_noise
    
mean_10 = total/10


for i in range (100):
    noise = np.random.normal(0, 3, len(vector_t))
    signal_with_noise = signal + noise
    total += signal_with_noise
    
mean_100 = total/100

for i in range (1000):
    noise = np.random.normal(0, 3, len(vector_t))
    signal_with_noise = signal + noise
    total += signal_with_noise
    
mean_1000 = total/1000

# =============================================================================
#                              PLOTEO
# =============================================================================

fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
axs[0, 0].plot(vector_t, signal)
axs[0, 0].set_title(r'$x(t)$')
axs[0, 1].plot(vector_t, mean_10, color='orange')
axs[0, 1].set_title('Promedio de 10')
axs[1, 0].plot(vector_t, mean_100, color='green')
axs[1, 0].set_title('Promedio de 100')
axs[1, 1].plot(vector_t, mean_1000, color='black')
axs[1, 1].set_title('Promedio de 1000')
fig.tight_layout()

for ax in axs.flat:
    ax.set(xlabel='Tiempo [s]', ylabel='Amplitud')
    ax.grid()
    
plt.show()

