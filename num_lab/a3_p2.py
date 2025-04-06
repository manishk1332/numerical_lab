import math
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 0.5, 1, 1.5, 2, 2.5], dtype=np.float64)
y = np.array([0, 0.2, 0.27, 0.3, 0.32, 0.33], dtype=np.float64)

n = 3

A = np.zeros((n+1, n+1), dtype=np.float64)
B = np.zeros((n+1, 1), dtype=np.float64)

for i in range(n+1):
    for j in range(n+1):
        A[i][j] = np.sum(np.power(x, i+j))

for i in range(n+1):
    B[i][0] = np.sum(np.multiply(np.power(x, i), y))

X = np.linalg.solve(A, B)
print(X)

pt = np.array(np.linspace(0, 2.5, 251), dtype=np.float64)
Y = np.zeros(np.shape(pt), dtype=np.float64)

for i in range(n+1):
    Y = np.add(Y, np.array((X[i][0]*np.power(pt, i)), dtype=np.float64))


# Plotting the curve and points
plt.plot(pt, Y, label='Fitted Line', color='blue')  # Plot the curve
plt.scatter(x, y, label='Data Points', color='red')  # Plot the points
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Fit')
plt.legend()
plt.grid(True)
plt.show()