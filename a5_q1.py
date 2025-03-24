import numpy as np
import matplotlib.pyplot as plt

def u0(x):
    if -1/3 < x < 1/3:
        return 1
    else:
        return 0

def solve(n, m, x, t):
    u = np.zeros(n + 1)
    for i in range(n + 1):
        u[i] = u0(x[i])

    v = np.zeros(n + 1)

    for _ in range(m):
        for i in range(1, n):
            v[i] = 0.1 * u[i + 1] + 0.9 * u[i - 1]
        v[0] = 0.1 * u[1] + 0.9 * u[n - 1]
        v[n] = 0.1 * u[1] + 0.9 * u[n - 1]
        u[:] = v  

    for i in range(n + 1):
        print(f'u({x[i]}, 4) = {u[i]}')
    
    plt.plot(x, u)
    plt.show()

n = 200
a = -1.0
b = 1.0
dx = (b - a) / n
dt = 0.8 * dx
m = int(4 / dt)  # 500

x = np.linspace(a, b, n + 1)
t = np.linspace(0, 4, m + 1)

solve(n, m, x, t)

n = 5000
a = -1.0
b = 1.0
dx = (b - a) / n
dt = 0.8 * dx
m = int(4 / dt)

x2 = np.linspace(a, b, n + 1)
t2 = np.linspace(0, 4, m + 1)

#solve(n, m, x2, t2)
