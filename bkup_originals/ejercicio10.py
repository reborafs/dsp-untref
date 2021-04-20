# -*- coding: utf-8 -*-

# Convolucionar linealmente la señal Midi69.wav (buscarla en la carpeta del aula virtual) con la
# respuesta al impulso resp_imp.wav (en la misma carpeta). Luego convolucionar en forma circular
# las dos señales con un largo igual a la señal respuesta al impulso. Finalmente, calcular con
# convolución circular modificando las señales de forma tal de que el resultado sea igual a la
# convolución lineal. En todos los casos, graficar las señales convolucionadas y generar los archivos
# .wav correspondientes.

import numpy as np
from matplotlib import pyplot as plt
import sounddevice as sd
import soundfile as sf
from scipy import signal
import time

signal, fs1 = sf.read("Midi69.wav")  #Midi69.wav
respuesta_impulso, fs2 = sf.read("Resp_Imp.wav") #resp_imp.wav

if len(signal) > len(respuesta_impulso):
    period = len(signal)
    
elif len(signal) < len(respuesta_impulso):
    period = len(respuesta_impulso)
    
else:
    period = len(respuesta_impulso)
    

# =============================================================================
#                   CONVOLUCION LINEAL
# =============================================================================


conv_lineal = np.convolve(signal, respuesta_impulso)

plt.plot(np.arange(0, len(conv_lineal)/fs1, 1/fs1) ,conv_lineal)
plt.show()

# sd.play(signal/abs(max(signal)), fs1)
# sd.wait()
# sd.play(convo_lineal/abs(max(convo_lineal)), fs1)
# sd.wait()


# =============================================================================
#                   CONVOLUCION CIRCULAR
# =============================================================================

def circular_convolve(in1, in2, period):
    """
    Circular convolution of two 1-dimensional arrays.
    Circular convolve `in1` and `in2` with given `period`.
    Parameters
    ----------
    in1 : array_like, 1-D
        First input.
    in2 : array_like, 1-D
        Second input. Should have the same number of dimensions as `in1`.
    period : int
        Period of the circular convolution.
    Returns
    -------
    result : array, 1-D
        A 1-dimensional array containing the result of the circular
        convolution of `in1` with `in2`.
    See Also
    --------
    convolve
    Notes
    -----
    The (modulo-M) circular/cyclic/periodic convolution of period :math:`M`
    of the two signals :math:`x[k]` and :math:`h[k]` is defined as
    .. math::
        y[k] = \sum_{\kappa=0}^{M-1} \tilde{x}[k - \kappa] \; \tilde{h}[\kappa]
    where the periodic summations :math:`\tilde{x}[k]` and `\tilde{h}[\kappa]`
    of :math:`x[k]` and :math:`x[k]` are defined as
    .. math::
        \tilde{x}[k] &= \sum_{m = -\infty}^{\infty} x[m \cdot M + k] \\
        \tilde{h}[k] &= \sum_{m = -\infty}^{\infty} h[m \cdot M + k]
    Examples
    --------
    Equivalence of circular and linear convolution:
    >>> from scipy import signal
    >>> a = np.ones(5)
    >>> b = np.ones(5)
    >>> circular_convolve(a, b, 5)
    array([ 5.,  5.,  5.,  5.,  5.])
    >>> np.convolve(a, b, mode='full')
    array([ 1.,  2.,  3.,  4.,  5.,  4.,  3.,  2.,  1.])
    >>> circular_convolve(a, b, 9)
    array([ 1.,  2.,  3.,  4.,  5.,  4.,  3.,  2.,  1.])
    """
    in1 = _periodic_summation(in1, period)
    in2 = _periodic_summation(in2, period)

    return np.fromiter([np.dot(np.roll(in1[::-1], k+1), in2)
                        for k in np.arange(period)], float)

def _periodic_summation(x, period):
    """
    Periodic summation of 1-dimensional array or zero-padding.
    If the length of the array is longer or equal to the given `period`
    a periodic summation of `x` is perfomed, otherwise zero-padding to length
    `period`.
    """
    len_x = len(x)
    rows = int(np.ceil(len_x/period))

    if (len_x < int(period*rows)):
        x = np.pad(x, (0, int(period*rows-len_x)), 'constant')

    x = np.reshape(x, (rows, period))

    return np.sum(x, axis=0)


conv_circular = circular_convolve(signal, respuesta_impulso, period)

plt.plot(np.arange(0, len(conv_circular)/fs1, 1/fs1) ,conv_circular)
plt.show()

# =============================================================================
#                   CONVOLUCION CIRCULAR CON ZERO PADDING
# =============================================================================

def conv_zero_padding(in1, in2):
    
    in1 = np.copy(signal)
    in2 = np.copy(respuesta_impulso)
    
    N = len(in1) + len(in2) - 1        
    
    zeros_1 = np.zeros(N - len(in1))
    in1 = np.hstack((in1, zeros_1))
    
    
    zeros_2 = np.zeros(N - len(in2))
    in2 = np.hstack((in2, zeros_2))
    
    return in1, in2


in1, in2 = conv_zero_padding(signal, respuesta_impulso)

period = len(in2)

conv_circular_ceros = circular_convolve(in1, in2, period)

check = (conv_circular_ceros == conv_lineal)

plt.plot(np.arange(0, len(conv_circular_ceros)/fs1, 1/fs1) ,conv_circular_ceros)
plt.show()
