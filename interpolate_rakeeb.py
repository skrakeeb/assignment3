"""coded by: rakeeb
    purpose: to study interpolation by various techniques"""



import numpy as np 
import scipy.interpolate as spi
import matplotlib.pyplot as plt 

x= np.array([0,1,2,3,4,5])
y= np.array([1.0,2.0,1.0,0.5,4.0,8.0])

uspl= spi.interp1d(x,y,kind='slinear', fill_value='extrapolate')    #univariate spline
bspl= spi.interp1d(x,y,kind='quadratic', fill_value='extrapolate')  #bivariate spline 
cspl= spi.CubicSpline(x,y)                                          #cubic spline
lint= spi.lagrange(x,y)                                             #lagrange interpolation 

xnew= np.arange(0,5,0.001)
y_u= uspl(xnew)
y_b= bspl(xnew)
y_c= cspl(xnew)
y_l= lint(xnew)

plt.plot(x,y,'o', color='red')
plt.plot(xnew,y_u,'-',color='blue',label='univariate spline')
plt.plot(xnew,y_b,'-',color='orange',label='bivariant spline')
plt.plot(xnew,y_c,'-',color='green',label='cubic spline')
plt.plot(xnew,y_l,'-',color='violet',label='lagrange interpolatio')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()
