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

for i in range(n+1):
    if(x[i]<=0.5): u[0][i] = 2*x[i]
    else: u[0][i] = 2*(1-x[i])

for i in range(1, 201):
    for j in range(1, n):
        u[i][j]=u[i-1][j]+(dt/(dx*dx))*(u[i-1][j-1]-2*u[i-1][j]+u[i-1][j+1])

print(u[50])
plt.plot(x, u[50], label='At t=50 steps', color='blue')
plt.xlabel('x')
plt.ylabel('u')
plt.legend()
plt.grid(True)
plt.show()

print(u[100])
plt.plot(x, u[100], label='At t=100 steps', color='blue')
plt.xlabel('x')
plt.ylabel('u')
plt.legend()
plt.grid(True)
plt.show()

print(u[200])
plt.plot(x, u[200], label='At t=200 steps', color='blue')
plt.xlabel('x')
plt.ylabel('u')
plt.legend()
plt.grid(True)
plt.show()