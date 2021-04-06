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

signal, fs1 = sf.read("cumbia.wav")  #Midi69.wav
respuesta_impulso, fs2 = sf.read("respuesta.wav") #resp_imp.wav

convo_lineal = np.convolve(signal, respuesta_impulso[0,:])

plt.figure()
plt.plot(np.arange(0, len(convo_lineal)/fs1, 1/fs1) ,convo_lineal)

# sd.play(signal/abs(max(signal)), fs1)
# sd.wait()
# sd.play(convo_lineal/abs(max(convo_lineal)), fs1)
# sd.wait()