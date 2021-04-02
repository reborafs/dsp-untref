# -*- coding: utf-8 -*-
"""
@author: franco
"""

import numpy as np
import matplotlib.pyplot as plt

fs = 44100
t = 1

vector_t = np.linspace(0,t,t*fs)

u2 = 0.2
sigma2 = 0.05
exp2 = ((vector_t-u2)**2)/(2*(sigma2**2))

u3 = 0.7
sigma3 = 0.07
exp3 = ((vector_t-u3)**2)/(2*(sigma3**2))

x1 = 2*np.ones_like(vector_t)
x2 = np.e**(-exp2)
x3 = np.e**(-exp3)

xt = x1 + x2 + x3

fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
axs[0, 0].plot(vector_t, x1)
axs[0, 0].set_title('x1(t)')
axs[0, 1].plot(vector_t, x2, 'tab:orange')
axs[0, 1].set_title('x2(t)')
axs[1, 0].plot(vector_t, x3, 'tab:green')
axs[1, 0].set_title('x3(t)')
axs[1, 1].plot(vector_t, xt, 'tab:red')
axs[1, 1].set_title('x1(t)+x2(t)+x3(t)')
fig.tight_layout()

for ax in axs.flat:
    ax.set(xlabel='Tiempo [s]', ylabel='Amplitud')
    ax.grid()
    
plt.show()

def derivada_discreta(x,vector_t):

    f_de_x = np.zeros(len(vector_t))
    
    for i in range(len(x)-1):
        
        f_de_x[i] = (x[i+1]-x[i])/(vector_t[i+1]-vector_t[i])
    
    return f_de_x
    
f_x1 = derivada_discreta(x1, vector_t)
f_x2 = derivada_discreta(x2, vector_t)
f_x3 = derivada_discreta(x3, vector_t)
f_t = derivada_discreta(xt, vector_t)



fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
axs[0, 0].plot(vector_t, f_x1)
axs[0, 0].set_title(r'$f´(x_{1})$')
axs[0, 1].plot(vector_t, f_x2, 'tab:orange')
axs[0, 1].set_title(r'$f´(x_{2})$')
axs[1, 0].plot(vector_t, f_x3, 'tab:green')
axs[1, 0].set_title(r'$f´(x_{3})$')
axs[1, 1].plot(vector_t, f_t, 'tab:red')
axs[1, 1].set_title(r'$f´(x_{t})$')
fig.tight_layout()

for ax in axs.flat:
    ax.set(xlabel='Tiempo [s]', ylabel='Amplitud')
    ax.grid()
    
plt.show()

# =============================================================================
#                       Xt + Ruido
# =============================================================================

ruido = 0.01*np.random.normal(0,0.01, len(vector_t))

x_with_noise = xt + ruido
x_with_noise = x_with_noise/abs(max(x_with_noise))

f_x_with_noise = derivada_discreta(x_with_noise, vector_t)
f_x_with_noise = f_x_with_noise/abs(max(f_x_with_noise))


plt.figure()
plt.plot(vector_t,f_x_with_noise,'orange')
plt.plot(vector_t, x_with_noise)
plt.title(r'$f´(x_{noise})$')
plt.xlabel('tiempo[s]')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()