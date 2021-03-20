# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 15:51:23 2021

@author: luna
"""


import numpy as np

def valor_medio(x):
    N = np.len(x)
    u= np.dot((1/N), (np.sum(x, initial=0, where= N-1)))
    return u

def desvio_medio(x,u):
    N=np.len(x)
    d= np.dot((1/N),(np.sum(np.absolute(x-u), initial= 0, where= N)))
    return d

def desvio_estandar(x,u):
    N=np.len(x)
    tau= np.dot((1/N),(np.sum(np.absolute((x-u)**2), initial= 0, where= N)))ç
    var= tau**2
    return tau, var 

def rms(x):
    N=np.len(x)
    rms= sqrt(np.dot((1/N),(np.sum(np.absolute(x**2), initial= 0, where= N)))
    return rms
    