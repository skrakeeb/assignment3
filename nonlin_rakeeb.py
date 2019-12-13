"""coded by: rakeeb
   purpose: root finding by various methods"""



import numpy as np 
import scipy.optimize as spo
from math import *
def f(x):
	return sin(cos(exp(x)))

root=spo.bisect(f,-1,1)
print("the root of the given eqn by bisection method : ",root)
print("value at the root point: ",sin(cos(exp(root))))


root=spo.newton(f,-1)
print("the root of the given eqn by Newton Raphson method taking -1 as initial point: ",root)
print("value at the root point: ",sin(cos(exp(root))))

root=spo.newton(f,-0.1)
print("the root of the given eqn by Newton Raphson method taking -1 as initial point: ",root)
print("value at the root point: ",sin(cos(exp(root))))