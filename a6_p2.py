import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


g = 9.81
h, u = sp.symbols('h u')

m = sp.Matrix([[0,1],[g*h-u**2, 2*u]])
eigenvalues = m.eigenvals()

e1, e2 = list(eigenvalues)


n = 500
a = 0
b = 5
dx = (b-a) / n
x = np.linspace(a, b, n+1)

T = 1
time = [0]


def spectral_rad(t):
    max_val = -1
    for i in range(n+1):
        temp_max = max(abs(u[i,t]+np.sqrt(g*h[i,t])), abs(u[i,t]-np.sqrt(g*h[i,t])))
        max_val = max(temp_max, max_val)
    return max_val  

# u(x, t)
u = np.zeros((n+1, 1000))
# h(x, t)
h = np.zeros((n+1, 1000))

for i in range(n+1):
    if((a+i*dx)<2.5) : h[i, 0] = 2
    else : h[i, 0] = 1
    u[i ,0] = 0


time_val = 0
for t in range(1001):
    dt = (0.9*dx)/(spectral_rad(t))
    time_val = time_val + dt
    if time_val > T:
        break
    time.append(time[-1]+dt)
    for i in range(n+1):
        l = i-1
        r = i+1
        if l == -1:
            l = 0
        if r == n+1:
            r = n
        
        h[i, t+1] = (h[r, t] + h[l, t])/2  - dt*(h[r, t]*u[r,t] - h[l,t]*u[l,t])/(2*dx) 
        u[i, t+1] = (h[r, t]*u[r,t] + h[l,t]*u[l,t])/(2*h[i, t+1]) - dt*(h[r,t]*u[r,t]**2+0.5*g*h[r,t]**2 - (h[l,t]*u[l,t]**2+0.5*g*h[l,t]**2))/(2*dx*h[i, t+1]) 
    
time_val = time_val - dt
print(time_val)
m = len(time)-1

plt.plot(x, u[:, m])
plt.show()
plt.plot(x, h[:, m])
plt.show()
'''
for t in range(m+1):
    plt.plot(x, u[:, t])
plt.show()

for t in range(m+1):
    plt.plot(x, h[:, t])
plt.show()
'''