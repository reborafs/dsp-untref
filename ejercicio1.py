# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

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



fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
axs[0, 0].plot(vector_t, x1)
axs[0, 0].set_title('x1(t)')
axs[0, 1].plot(vector_t, x2, color='orange')
axs[0, 1].set_title('x2(t)')
axs[1, 0].plot(vector_t, x3, color='green')
axs[1, 0].set_title('x3(t)')
axs[1, 1].plot(vector_t, x1+x2+x3, color='black')
axs[1, 1].set_title('x1(t)+x2(t)+x3(t)')
fig.tight_layout()

for ax in axs.flat:
    ax.set(xlabel='Tiempo [s]', ylabel='Amplitud')
    ax.grid()
