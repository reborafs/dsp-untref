# -*- coding: utf-8 -*-

import numpy as np
from scipy.signal import convolve
from matplotlib import pyplot as plt
import sounddevice as sd


def mediamovil_conv(x, M):
    '''
    Scipy implementation of a moving average filter with a convolutional method.
    The resulting filtered sample is calculated with a convolution between the
    original signal and a rectangular pulse with length 'M'.

    Parameters
    ----------
    x : ndarray
        Input signal. 
    M : int
        Window length.

    Returns
    -------
    y : ndarray
        Output filtered signal.

    '''
    h = np.ones(M)/M
    y = convolve(x,h)
    return y


# t = 3
# fs = 44100
# vector_t = np.linspace(0,t,t*fs)
# signal = np.sin(2*np.pi*500*vector_t)
# noise = 0.1*np.random.normal(0,0.5, len(vector_t))
# x = signal + noise

# y = mediamovil_conv(x, 5)

# plt.plot(x)
# plt.plot(y)

# sd.play(signal,fs)
# sd.wait()
# sd.play(x,fs)
# sd.wait()
# sd.play(y,fs)
# sd.wait()