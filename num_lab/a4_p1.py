import numpy as np
import math

a = 0.0
b = 1.0

h = 0.1

n = int((b-a)/h)

y0=-1
y10=0

x = np.linspace(0,1,11, dtype=np.float64)

def D(x):
    return np.exp(x)

def E(x):
    return -1*x

def f(x):
    return (-x*x+2*x-3)*np.exp(-1*x)-x+2

A = np.zeros((n-1, n-1), dtype=np.float64)

for i in range(0,n-1):
    if(i>0): A[i][i-1] = 1-(0.5*h)*D(x[i+1])
    A[i][i] = h*h*E(x[i+1])-2
    if(i<n-2): A[i][i+1] = 1+(0.5*h)*D(x[i+1])

B = np.zeros((n-1, 1), dtype=np.float64)

B[0][0] = h*h*f(x[1]) - y0*(1-0.5*h*D(x[1]))
B[n-2][0] = h*h*f(x[n-1]) - y10*(1+0.5*h*D(x[n-1]))

for i in range(1,n-2):
    B[i][0] = h*h*f(x[i+1])

X = np.linalg.solve(A, B)

exact = (x-1)*np.exp(-1*x)
print(exact.tolist())
print(X.tolist())