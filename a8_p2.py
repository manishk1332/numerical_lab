import numpy as np
import matplotlib.pyplot as plt


n = 50
a = 0
b = 1

m = 600

dx = (b-a) / n
dt = (0.9 * (dx)**2) / 2

x = np.linspace(a, b, n+1)
t = np.linspace(0, dt*m, m+1)

# u(x, t)
u = np.zeros((n+1, m+1))

for i in range(n+1):
    if (a+i*dx) <= 1/2:
        u[i, 0] = 2*(a+i*dx)
    elif 1/2 <= (a+i*dx): 
        u[i, 0] = 2*(1-(a+i*dx))

for t in range(m):
    for i in range(n+1):
        if (a+i*dx) == a:
            u[i, t+1] = 0
        elif (a+i*dx) == b:
            u[i, t+1] = 0
        else:
            u[i, t+1] = u[i, t] +  dt*(u[i+1, t] - 2*u[i, t] + u[i-1, t]) / dx**2 
    

for t in [0, 50, 100, 200]:
    plt.plot(x, u[:, t])
    plt.legend([0, 50, 100, 200])

plt.show()