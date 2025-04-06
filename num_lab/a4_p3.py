import numpy as np
import math

def f(x,y,z):
    return z

def p(x,y,z):
    return (3/x)*z-(3/(x*x))*y+2*x*x*np.exp(x)

def RK(h, x, y, z):
    k1 = h*f(x,y,z)
    l1 = h*p(x,y,z)
    k2 = h*f(x+0.5*h, y+0.5*k1, z+0.5*l1)
    l2 = h*p(x+0.5*h, y+0.5*k1, z+0.5*l1)
    k3 = h*f(x+0.5*h, y+0.5*k2, z+0.5*l2)
    l3 = h*p(x+0.5*h, y+0.5*k2, z+0.5*l2)
    k4 = h*f(x+h, y+k3, z+l3)
    l4 = h*p(x+h, y+k3, z+l3)
    k = (k1+2*k2+2*k3+k4)/6
    l = (l1+2*l2+2*l3+l4)/6
    return y+k, z+l

a = 1.0
b = 2.0
h = 0.1
n = int((b-a)/h)
g1 = 0
g2 = 4*np.exp(1)*np.exp(1)

x = np.linspace(a,b,n+1)
u=[0]
w=[0]

for i in range(n):
    u_n, w_n = RK(h, x[i], u[i], w[i])
    u.append(u_n)
    w.append(w_n)

v=[0]
z=[1]

for i in range(n):
    v_n, z_n = RK(h, x[i], v[i], z[i])
    v.append(v_n)
    z.append(z_n)

print(u, v)

lmd = (g2-v[-1])/(u[-1]-v[-1])

u = np.array(u)
v = np.array(v)

y_comp = lmd*u+(1-lmd)*v
y_exact = 2*x*np.exp(x)*(x-1)

print(y_comp)
print(y_exact)