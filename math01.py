import numpy as np  
import matplotlib.pyplot as plt  
	
def f(x):
	return 3*(x**13-1)/(x-1) - 156
	
def bisection(a,b,tol):
	c = (a+b)/2.0
	while (b-a)/2.0 > tol:
		if f(c) == 0:
			return c
		elif f(a)*f(c) < 0:
			b = c
		else :
			a = c
		c = (a+b)/2.0
	return c

y = bisection(1.01,2, 0.001)	
z = f(y)
print(y)
print(z)

a = np.arange(1.1, 2.0, 0.1)
b= 3*(a**13-1)/(a-1) - 156
print(b)
plt.figure(1)	
plt.plot(a, b)
plt.show()
print('bye')