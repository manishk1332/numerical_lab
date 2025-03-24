import numpy as np
import matplotlib.pyplot as plt
import sympy as sp



r, u = sp.symbols('rho u')

m = sp.Matrix([[0,1],[-u**2, 2*u]])
eigenvalues = m.eigenvals()

e1 = e2 = list(eigenvalues)[0]

eigenvectors = m.eigenvects()
eigenvec = eigenvectors[0][2][0]
print(e1, eigenvec)

n = 200
a = -1
b = 1
dx = (b-a) / n
x = np.linspace(a, b, n+1)

T = 0.5
time = [0]


def spectral_rad(t):
    max_val = -1
    for i in range(n+1):
        max_val = max(abs(u[i,t]), max_val)
    return max_val  

# u(x, t)
u = np.zeros((n+1, 1000))
# r(x, t)
r = np.zeros((n+1, 1000))

for i in range(n+1):
    if (a+i*dx) < 0:
        u[i, 0] = 2
    elif (a+i*dx) > 0:
        u[i, 0] = -2

    r[i ,0] = 1

time_val = 0
for t in range(1001):
    dt = (0.8*dx)/(spectral_rad(t))
    time_val = time_val + dt
    if time_val > T:
        break
    time.append(time[-1]+dt)
    for i in range(n+1):
        l = i-1
        ri = i+1
        if l == -1:
            l = 0
        if ri == n+1:
            ri = n
        
        r[i, t+1] = (r[ri, t] + r[l, t])/2  - dt*(r[ri, t]*u[ri,t] - r[l,t]*u[l,t])/(2*dx) 
        u[i, t+1] = (r[ri, t]*u[ri,t] + r[l,t]*u[l,t])/(2*r[i, t+1]) - dt*(r[ri,t]*u[ri,t]**2 - (r[l,t]*u[l,t]**2))/(2*dx*r[i, t+1]) 
    
time_val = time_val - dt

m = len(time)-1

for t in range(m+1):
    plt.plot(x, u[:, t])
plt.show()

for t in range(m+1):
    plt.plot(x, r[:, t])
plt.show()
