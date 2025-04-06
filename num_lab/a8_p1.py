import numpy as np
import matplotlib.pyplot as plt

a = 0.0
b = 1.0
dx = 0.02
n = int((b-a)/dx)
F = 0.9
dt = F*dx*dx*0.5

x = np.linspace(a, b, n+1)

u = np.zeros((501, n+1), dtype=np.float64)

u[0] = np.sin(np.pi*x)

for i in range(1, 501):
    for j in range(1, n):
        u[i][j]=u[i-1][j]+(dt/(dx*dx))*(u[i-1][j-1]-2*u[i-1][j]+u[i-1][j+1])

print(u[300])
plt.plot(x, u[300], label='At t=300 steps', color='blue')
plt.xlabel('x')
plt.ylabel('u')
plt.legend()
plt.grid(True)
plt.show()

print(u[400])
plt.plot(x, u[400], label='At t=400 steps', color='blue')
plt.xlabel('x')
plt.ylabel('u')
plt.legend()
plt.grid(True)
plt.show()

print(u[500])
plt.plot(x, u[500], label='At t=500 steps', color='blue')
plt.xlabel('x')
plt.ylabel('u')
plt.legend()
plt.grid(True)
plt.show()