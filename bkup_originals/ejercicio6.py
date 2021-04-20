# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

def mediamovild(x,M):
    '''
    This function implements a moving average filter with a direct method.
    The resulting filtered sample is calculated with the mean between the
    same sample in the original signal plus the length of the window 'M'.

    Parameters
    ----------
    x : ndarray
        Input signal. 
    M : int
        Window length.

    Returns
    -------
    filtered_signal : ndarray
        Output filtered signal.
    '''
    filtered_signal = np.zeros(len(x)-M+1)
    for i in range(len(x)-M+1):
        filtered_signal[i] = np.sum(x[i:i+M])/(M+1)
    return filtered_signal

def mediamovildr(x,M):
    '''
    This function implements a moving average filter with a recursive method.
    
    
    Parameters
    ----------
    x : ndarray
        Input signal. 
    M : int
        Window length, must be an odd integer.

    Returns
    -------
    filtered_signal : ndarray
        Output filtered signal.
    '''
    filtered_signal = np.zeros(len(x)-M+1)
    filtered_signal[0] = np.sum(x[:M])
    
    P = int((M-1)/2)
    for i in range(1, len(x)-M+1):
        filtered_signal[i] = filtered_signal[i-1] + x[i + P] - x[i -(P+1)]
    
    filtered_signal = filtered_signal/(M+1)
    return filtered_signal

# CUIDADO: HAY QUE FIJARSE SI ESTA BIEN QUE LA SENAL ARRANQUE EN CERO PARA 
# EL METODO RECURSIVO PORQUE, EN REALIDAD, AL USAR EL METODO SIMETRICO 
# DEBERIA ARRANCAR EN LA MITAD DE LA VENTANA.


# =============================================================================
#                           TEST
# =============================================================================

#   METODO DIRECTO

# window_len = 10
# fs = 44100
# t = 3
# vector_t = np.linspace(0,t,t*fs)
# signal = np.sin(2*np.pi*500*vector_t)
# noise = 0.1*np.random.normal(0,0.5, len(vector_t))
# signal_with_noise = signal + noise
# signal_with_noise = signal_with_noise/max(abs(signal_with_noise))

# filtered_signal = mediamovild(signal_with_noise, window_len)
# filtered_signal = filtered_signal/max(abs(filtered_signal))

# fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
# axs[0].plot(vector_t, signal_with_noise)
# axs[0].set_title(r'$x(t) + noise$')
# axs[1].plot(vector_t[:-window_len+1], filtered_signal, color='green')
# axs[1].set_title('Filtro de media movil: Metodo directo')
# fig.tight_layout()
    
#   METODO RECURSIVO
    
# window_len = 101
# fs = 44100
# t = 3
# vector_t = np.linspace(0,t,t*fs)
# signal = np.sin(2*np.pi*1000*vector_t)
# noise = 0.1*np.random.normal(0,0.5, len(vector_t))
# signal_with_noise = signal + noise
# x = signal_with_noise

# filtered_signal = mediamovildr(x, window_len)
# filtered_signal = filtered_signal/max(abs(filtered_signal))


# fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
# axs[0].plot(vector_t, x)
# axs[0].set_title(r'$x(t) + noise$')
# axs[1].plot(vector_t[:-window_len+1], filtered_signal, color='green')
# axs[1].set_title('Filtro de media movil: Metodo recursivo')
# fig.tight_layout()


# =============================================================================
#                       TEST DE AUDIO
# =============================================================================

# sd.play(signal,fs)
# sd.wait()
# sd.play(signal_with_noise,fs)
# sd.wait()
# sd.play(filtered_signal,fs)
# sd.wait()

