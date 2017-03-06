import numpy as np
import pylab as pl

#generate array of 100 evenly spaced numbers for 0 to 4*pi
x = np.linspace(0,4*np.pi,100)

#create another array that is equal to sin(x)
y = np.sin(x)

#plot the two arrays against one another
pl.plot(x,y)
pl.xlabel('x')
pl.ylabel('sin(x)')
pl.show()
