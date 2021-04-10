# -*- coding: utf-8 -*-

import numpy as np

# =============================================================================
# Funciones utilizadas en los ejercicios 1 a 5
# =============================================================================
def valor_medio(x):
    '''
    

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.

    Returns
    -------
    u : TYPE
        DESCRIPTION.

    '''
    u = (1/len(x))*np.sum(x)
    return u

def desvio_medio(x):
    '''
    

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.

    Returns
    -------
    d : TYPE
        DESCRIPTION.

    '''
    N = len(x)
    u = (1/N)*np.sum(x)
    d = (1/N)*np.sum(abs(x-u))
    return d

def desvio_estandar(x):
    '''
    

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.

    Returns
    -------
    tau : TYPE
        DESCRIPTION.

    '''
    N = len(x)
    u = (1/N)*(np.sum(x))
    tau = np.sqrt((1/(N-1))*(np.sum(abs((x-u)**2))))
    return tau 

def rms(x):
    '''
    

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.

    Returns
    -------
    rms : TYPE
        DESCRIPTION.

    '''
    N = len(x)
    rms = np.sqrt((1/N)*np.sum(abs(x**2)))
    return rms
    
# =============================================================================
# Funciones utilizadas en el ejercicio 6
# =============================================================================

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


def conv_zero_padding(in1, in2):
    '''
    

    Parameters
    ----------
    in1 : TYPE
        DESCRIPTION.
    in2 : TYPE
        DESCRIPTION.

    Returns
    -------
    in1 : TYPE
        DESCRIPTION.
    in2 : TYPE
        DESCRIPTION.

    '''
    
    in1 = np.copy(signal)
    in2 = np.copy(respuesta_impulso)
    
    N = len(in1) + len(in2) - 1        
    
    zeros_1 = np.zeros(N - len(in1))
    in1 = np.hstack((in1, zeros_1))
    
    
    zeros_2 = np.zeros(N - len(in2))
    in2 = np.hstack((in2, zeros_2))
    
    return in1, in2

# =============================================================================
# Funciones utilizadas en el ejercicio 7
# =============================================================================


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

# =============================================================================
#  Funciones utilizadas en el ejercicio 8
# =============================================================================

def blackmanfilt(x, M, a0=0.42, a1=0.5, a2=0.08):
    '''
    

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    M : TYPE
        DESCRIPTION.
    a0 : TYPE, optional
        DESCRIPTION. The default is 0.42.
    a1 : TYPE, optional
        DESCRIPTION. The default is 0.5.
    a2 : TYPE, optional
        DESCRIPTION. The default is 0.08.

    Returns
    -------
    y : TYPE
        DESCRIPTION.

    '''
    n = np.arange(M)
    blackman = a0+a1*np.cos(2*np.pi*n/(M-1))+a2*np.cos(4*np.pi*n/(M-1))
    y = convolve(x,blackman)
    y = y/max(abs(y))
    return y


# =============================================================================
#  Funciones utilizadas en el ejercicio 9
# =============================================================================

def derivada_discreta(x,vector_t):
    '''
    

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    vector_t : TYPE
        DESCRIPTION.

    Returns
    -------
    f_de_x : TYPE
        DESCRIPTION.

    '''
    f_de_x = np.zeros(len(vector_t))
    
    for i in range(len(x)-1):
        
        f_de_x[i] = (x[i+1]-x[i])/(vector_t[i+1]-vector_t[i])
    
    return f_de_x
    