import numpy as np
import math
import matplotlib.pyplot as plt

def u(x):
    if(abs(x)<(1/3)): return 1
    else: return 0

def f(u):
    return u

a = -1.0
b = 1.0
n = 200
x = np.linspace(a,b,n+1)

dx = (b-a)/n
lmd = 0.8
dt = lmd*dx

u0 = []

for i in x:
    u0.append(u(i))

u = []
u.append(u0)

t=0
T=4
ts = 0
while(t<T):
    temp=[0]*(n+1)
    for i in range(1,n):
        temp[i] = 0.5*(u[ts][i+1]+u[ts][i-1]) - 0.5*(dt/dx)*(f(u[ts][i+1]) - f(u[ts][i-1]))

    temp[0] = 0.5*(u[ts][1]+u[ts][n-1]) - 0.5*(dt/dx)*(f(u[ts][1]) - f(u[ts][n-1]))
    temp[n] = 0.5*(u[ts][1]+u[ts][n-1]) - 0.5*(dt/dx)*(f(u[ts][1]) - f(u[ts][n-1]))

    u.append(temp)
    t+=dt
    ts+=1

print(u[-1])
plt.plot(x, u[-1], label='At t=4 units', color='blue')
plt.xlabel('x')
plt.ylabel('u')
plt.legend()
plt.grid(True)
plt.show()