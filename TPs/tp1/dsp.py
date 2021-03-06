# -*- coding: utf-8 -*-

import numpy as np
from scipy import signal
# =============================================================================
# Funciones utilizadas en los ejercicios 1 a 5
# =============================================================================
def valor_medio(x):
    '''
    Calcula el valor medio de un array utilizando la libreria numpy.

    Parameters
    ----------
    x : ndarray
        Array de entrada.


    Returns
    -------
    u : float
        Valor medio del array.
    '''
    u = (1/len(x))*np.sum(x)
    return u

def desvio_medio(x):
    '''
    Calcula el desvio medio de un array utilizando la libreria numpy.

    Parameters
    ----------
    x : ndarray
        Array de entrada.
    Returns
    -------
    d : float
        Desvio medio del array.
    '''
    N = len(x)
    u = (1/N)*np.sum(x)
    d = (1/N)*np.sum(abs(x-u))
    return d

def desvio_estandar(x):
    '''
    Calcula el desvio estandar de un array utilizando la libreria numpy.

    Parameters
    ----------
    x : ndarray
        Array de entrada.

    Returns
    -------
    tau : float
        Desvio estandar del array.

    '''
    N = len(x)
    u = (1/N)*(np.sum(x))
    tau = np.sqrt((1/(N-1))*(np.sum(abs((x-u)**2))))
    return tau 

def rms(x):
    '''
    Calcula el valor RMS de un array utilizando la libreria numpy.

    Parameters
    ----------
    x : ndarray
        Array de entrada.

    Returns
    -------
    rms : float
        Valor RMS del array.

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


def conv_zero_padding(signal, respuesta_impulso):
    '''
    Zero padding for two signals. Returns both signals with the same length.

    Parameters
    ----------
    signal : ndarray
        Input array
    respuesta_impulso : ndarray
        Input array.

    Returns
    -------
    in1 : ndarray
        Output array with zero padding if necessary.
    in2 : ndarray
        Output array with zero padding if necessary.

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
    y = np.convolve(x,h)
    return y

# =============================================================================
#  Funciones utilizadas en el ejercicio 8
# =============================================================================

def blackmanfilt(x, M, a0=0.42, a1=0.5, a2=0.08):
    '''
    Numpy implementation of a blackman filter with a convolutional method.
    The resulting filtered sample is calculated with a convolution between the
    original signal and a blackman window with length 'M'.
    
    Parameters
    ----------
    x : ndarray
        Input array.
    M : int
        Window length.
    a0 : float, optional
        First coefficient of the blackman window. The default is 0.42.
    a1 : float, optional
        Second coefficient of the blackman window. The default is 0.5.
    a2 : float, optional
        Second coefficient of the blackman window. The default is 0.08.

    Returns
    -------
    y : ndarray
        Filtered normalized signal.

    '''
    n = np.arange(M)
    blackman = a0+a1*np.cos(2*np.pi*n/(M-1))+a2*np.cos(4*np.pi*n/(M-1))
    y = np.convolve(x,blackman)
    y = y/max(abs(y))
    return y


# =============================================================================
#  Funciones utilizadas en el ejercicio 9
# =============================================================================

def derivada_discreta(x,vector_t):
    '''
    Calculates the discrete derivative of an array using the numpy library.    

    Parameters
    ----------
    x : ndarray
        Input array, refers to the ordinate values.
    vector_t : TYPE
        The time vector, refers to the abscissa values.

    Returns
    -------
    f_de_x : ndarray
        Discrete derivative.

    '''
    f_de_x = np.zeros(len(vector_t))
    
    for i in range(len(x)-1):
        
        f_de_x[i] = (x[i+1]-x[i])/(vector_t[i+1]-vector_t[i])
    
    return f_de_x
    
# =============================================================================
#  Funci??n utilizada para FFT en puntos 6, 7, 8 y 9.
# =============================================================================

def fft(x,t,Nfft):
    '''
    Approximate the Fourier transform of a finite duration signal 
    using scipy.signal.freqz()
    
    Parameters
    ----------
    x : input signal array
    t : time array used to create x(t)
    Nfft : the number of frdquency domain points used to 
           approximate X(f) on the interval [fs/2,fs/2], where
           fs = 1/Dt. Dt being the time spacing in array t
    
    Returns
    -------
    f : frequency axis array in Hz
    X : the Fourier transform approximation (complex)
    
    Notes
    -----
    The output time axis starts at the sum of the starting values in x1 and x2 
    and ends at the sum of the two ending values in x1 and x2. The default 
    extents of ('f','f') are used for signals that are active (have support) 
    on or within n1 and n2 respectively. A right-sided signal such as 
    :math:`a^n*u[n]` is semi-infinite, so it has extent 'r' and the
    convolution output will be truncated to display only the valid results.

    
    '''
    fs = 1/(t[1] - t[0])
    t0 = (t[-1]+t[0])/2 # time delay at center
    N0 = len(t)/2 # FFT center in samples
    f = np.arange(-1./2,1./2,1./Nfft)
    w, X = signal.freqz(x,1,2*np.pi*f)
    X /= fs # account for dt = 1/fs in integral
    X *= np.exp(-1j*2*np.pi*f*fs*t0)# time interval correction
    X *= np.exp(1j*2*np.pi*f*N0)# FFT time interval is [0,Nfft-1]
    F = f*fs
    
    return F, X
