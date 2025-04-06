import numpy as np
import math

def f(x,y,z):
    return z

def p(x,y,z):
    return (1-(z*z))/y

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

a = 0.0
b = 2.0
h = 0.4
n = int((b-a)/h)
g1 = 1
g2 = 2
s0 = 0
s1 = 2

x = np.linspace(a,b,n+1)

tol = 1e-4

while(abs(s1-s0)>tol):
    u=[1]
    w=[s0]

    for i in range(n):
        u_n, w_n = RK(h, x[i], u[i], w[i])
        u.append(u_n)
        w.append(w_n)

    v=[1]
    z=[s1]

    for i in range(n):
        v_n, z_n = RK(h, x[i], v[i], z[i])
        v.append(v_n)
        z.append(z_n)


    temp = s1 - ((s1-s0)/(v[-1]-u[-1]))*(v[-1]-g2)
    s0 = s1
    s1 = temp

print(s1)
y=[1]
q=[s1]

for i in range(n):
    y_n, q_n = RK(h, x[i], y[i], q[i])
    y.append(y_n)
    q.append(q_n)

print(y)
y_exact = np.sqrt(1 - 0.5*x + np.square(x))
print(y_exact)