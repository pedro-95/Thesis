import numpy as np
import pylab as plb
import matplotlib.pyplot as plt
import datetime
from scipy.optimize import curve_fit
from scipy import asarray as ar
from scipy.special import wofz
from scipy.constants import *
import scipy
import pylab
from matplotlib2tikz import save as tikz_save


def gaus_1(x,a,x0,sigma,off):
    return 1- a*np.exp(-(x-x0)**2/(2*sigma**2))+off

def gaus_2(x,a,x0,sigma,off):
    return 1- a*np.exp(-(x-x0)**2/(2*sigma**2))-0.25*x+off


x_1 = np.zeros(5000)
x_2 = np.zeros(5000)
for i in range (0,5000):
	x_1[i] = -5+i*0.001
	x_2[i] = i*0.001

plt.figure()
#plt.title('TOF Load MOT ')
#plt.ylabel('Phase space density')
#plt.xlabel('Evaporation end power /\% of \SI{63}{\watt}')
#plt.yscale("log", nonposy='clip')
#plt.xlim([0.7,1.6])
#plt.errorbar(evap_pow, trap_freq, trap_freq_err, color = 'red', marker = 'x', linestyle = '', label='Absorption')
plt.plot(x_1,gaus_1(x_1,1,0,1,0))
plt.plot(x_2,gaus_2(x_2,0.75,-0.25,1,-0.031))
#plt.legend()
plt.show()	


