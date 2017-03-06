"""
Fitting a general curve to data to optimize
"""

import scipy as sp
import scipy.optimize as opt
import random as random
import numpy as np
import pylab as pl

N = 1000	#number of data points
#Creating fake data to fit a straight line to:
x = np.random.uniform(low=-5, high=5., size=N)

#my own random 3rd order polynomial line 
#------------------------------------------------------------
def poly3(x):
	y=3.*x**3+2*x**2+5*x+6	
	yerr = np.random.normal(loc=0.,scale=15.,size=len(y)) #mean=0, std dev=15(or scatter)
	y = y+yerr
	return y	
#------------------------------------------------------------
#Create the function that will calculate the residuals:

def residuals(p,yy,xx):
	a,b,c,d = p
	err = abs(yy - (a**3*xx+b**2*xx+c**2*xx+d))
	return err

p0 = np.array([3.5,2.1,5.2,6.6])	#My own fake initial estimates for parameters a b c d (slightly different to actual)	
#print(residuals(p0,poly3(x),x))	

#Call the leasq() algorithm:
leastsqfit = opt.leastsq(residuals,p0,args=(poly3(x),x))	#leastsq(residual func,parameter estimates, arg=(y,x))
print("least square fit data:",leastsqfit)

coeffs = leastsqfit[0]

pl.plot(x,poly3(x),'bo')	#scatter plot
pl.show()
