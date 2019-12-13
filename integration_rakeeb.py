'''coded by : Sk Rakeeb
   coded for : study of integration by various methods'''


import numpy as np 
import scipy.integrate as spi 

x= np.arange(0,1.0,0.001)
y= np.exp(x)

trap= np.trapz(y,x)    #Trapezoidal rule
sim= spi.simps(y,x) #Simpson method


def f(x):
	return np.exp(x)

romb= spi.romberg(f,0,1)    #Romberg method
gauss= spi.fixed_quad(f,0,1,n=5)   #Gauss method

print("integration by Trapezoidal rule :",trap)
print("integration by Simpson's 1/3 rule :",sim)
print("integration by Romberg method :",romb)
print("integration by Gauss method :",gauss)
