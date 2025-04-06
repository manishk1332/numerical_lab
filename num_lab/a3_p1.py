import math
import numpy as np

x = np.array([1, 1.5, 2, 2.5, 3, 3.5, 4], dtype=np.float64)
y = np.array([25, 31, 27, 28, 36, 35, 32], dtype=np.float64)

A = np.zeros((2,2), dtype=np.float64)

A[0][0] = len(x)
A[0][1] = np.sum(x)
A[1][0] = np.sum(x)
A[1][1] = np.sum(np.square(x))

B = np.zeros((2,1), dtype=np.float64)

B[0][0] = np.sum(y)
B[1][0] = np.sum(np.multiply(x,y))

X = np.linalg.solve(A, B)

print(X)

pt = np.linspace(1, 4, 301)

Y = X[0][0] + X[1][0]*pt
import matplotlib.pyplot as plt  # Importing matplotlib for plotting

# Plotting the curve and points
plt.plot(pt, Y, label='Fitted Line', color='blue')  # Plot the curve
plt.scatter(x, y, label='Data Points', color='red')  # Plot the points
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Fit')
plt.legend()
plt.grid(True)
plt.show()