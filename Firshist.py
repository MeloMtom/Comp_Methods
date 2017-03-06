import numpy as np
import pylab as pl

#1000 Gaussian distributed random numbers 
#mean 5 and std dev 2:
R = np.random.normal(5,2,10000)

pl.hist(R,bins=30)
pl.show()
