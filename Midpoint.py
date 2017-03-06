"""
NASSP - CM
Author: Melo Mtombeni
Date:Feb 28 2017
Program to numerically integrate a 3rd order polynomial
"""
#Midpoint rule

import numpy as np
import pylab as pl

coeffs = input("Please enter 4 coefficients separated by spaces.\n")
coeffs = coeffs.split(' ')
coeffs = [float(i) for i in coeffs]

intrange = input("Please enter the range over which you want to integrate.\n")
intrange = intrange.split(' ')
intrange = [float(i) for i in intrange]

N = int(input("Please enter the number of segments for the domain\n"))

a = int(coeffs[0])
b = int(coeffs[1])
c = int(coeffs[2])
d = int(coeffs[3])

#coeff = np.array([a,b,c,d])
print(coeffs,intrange,N)

def poly3(x,a,b,c,d):
	return (a*(x**3))+(b*(x**2))+(c*x)+(d)

x = np.linspace(intrange[0],intrange[1],N)
#print(x)
pl.plot(x,poly3(x,a,b,c,d))
pl.vlines(x,0,poly3(x,a,b,c,d))
#pl.hlines(poly3(x,a,b,c,d)/2,x,0.5)
print(x)
for i in range(N-1):
	print(i)
	if(i<0):
		pl.hlines(poly3(x,a,b,c,d)[i],x[i],x[i-1])
	else:
		pl.hlines(poly3(x,a,b,c,d)[i],x[i],x[i-1])
pl.axvline(0,color='black')
pl.axhline(0,color='black')    
#pl.xlim(intrange[0],intrange[1])
pl.show()

