# -*- coding: utf-8 -*-

import numpy as np
from scipy.signal import convolve
from matplotlib import pyplot as plt
import sounddevice as sd


def blackmanfilt(x, M, a0=0.42, a1=0.5, a2=0.08):
    
    n = np.arange(M)
    blackman = a0+a1*np.cos(2*np.pi*n/(M-1))+a2*np.cos(4*np.pi*n/(M-1))
    y = convolve(x,blackman)
    y = y/max(abs(y))
    return y


# =============================================================================
#                           TEST
# =============================================================================

# t = 3
# fs = 44100
# M = 101
# vector_t = np.linspace(0,t,t*fs)

# signal = np.sin(2*np.pi*500*vector_t)
# noise = 0.1*np.random.normal(0,0.5, len(vector_t))
# x = signal + noise
# x = x/max(abs(x))

# y = blackmanfilt(x,M)

# plt.plot(x)
# plt.plot(y)

# sd.play(signal,fs)
# sd.wait()
# sd.play(x,fs)
# sd.wait()
# sd.play(y,fs)
# sd.wait()