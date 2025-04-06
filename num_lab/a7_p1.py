import numpy as np
import matplotlib.pyplot as plt
import math

#g = 9.81
a = -1.0
b = 1.0
dx = 0.01
n = int((b-a)/dx)
T = 0.5
t = 0

def h(x):
    return 1

def u(x):
    if(x<=0): return 2
    else: return -2

def sr(ts, u, h):
    n = len(u[ts])
    max_val = -1
    for i in range(n):
        temp_max = abs(u[ts][i])
        max_val = max(max_val, temp_max)
    return max_val



x = np.linspace(a, b, n+1)

u0 = []
for i in x:
    u0.append(u(i))

h0 = []
for i in x:
    h0.append(h(i))

u = []
u.append(u0)
h = []
h.append(h0)

ts = 0
while(t<T):
    dt = (0.9*dx)/sr(ts, u, h)
    ut = [0.0]*(n+1)
    ht = [0.0]*(n+1)
    for i in range(n+1):
        l = i-1
        r = i+1
        if(i==0): l=0
        if(i==n): r=n
        ht[i] = 0.5*(h[ts][r]+h[ts][l]) - (0.5*(dt/dx))*(u[ts][r]*h[ts][r]-u[ts][l]*h[ts][l])
        ut[i] = (0.5*(u[ts][r]*h[ts][r]+u[ts][l]*h[ts][l]))/(ht[i]) - (0.5*(dt/(dx*ht[i])))*((u[ts][r]**2*h[ts][r])-(u[ts][l]**2*h[ts][l]))

    u.append(ut)
    h.append(ht)
    t+=dt
    ts+=1    

print(u[-1])
plt.plot(x, u[-1], label='At t=1 units', color='blue')
plt.xlabel('x')
plt.ylabel('u')
plt.legend()
plt.grid(True)
plt.show()
print(h[-1])
plt.plot(x, h[-1], label='At t=1 units', color='blue')
plt.xlabel('x')
plt.ylabel('h')
plt.legend()
plt.grid(True)

plt.show()