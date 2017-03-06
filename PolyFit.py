"""
Fitting a polynomial to some data
"""

import numpy as np
import pylab as pl 
import scipy as sp

x = np.random.uniform(-5,5,50)
y = 2.2*x**2+3.5*x-4.5
yerr = np.random.normal(0.,4.5,len(x))
y = y+y_err

coeffs = sp.polyfit(x,y,z)
