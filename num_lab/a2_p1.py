import numpy as np
import math
import matplotlib.pyplot as plt

def f(x):
    return pow(x, 3)+2

x = np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0], dtype=np.float64)

a = np.power(x,3)+2

h=[]
for i in range(len(x)-1):
    h.append(x[i+1]-x[i])

n = len(x)

A = np.zeros((n, n), dtype=np.float64)
B = np.zeros((n, 1), dtype=np.float64)

A[0][0] = 1
A[n-1][n-1] = 1
for i in range(1,n-1):
    A[i][i-1] = h[i-1]
    A[i][i] = 2*(h[i-1]+h[i])
    A[i][i+1] = h[i]
    B[i] = 3*((a[i+1]-a[i])/h[i]-(a[i]-a[i-1])/h[i-1])

X = np.linalg.solve(A, B)

b = []

for i in range(n-1):
    temp = (a[i+1]-a[i])/h[i] - (h[i]/3)*(X[i+1][0]+2*X[i][0])
    b.append(temp)

d = []

for i in range(n-1):
    temp = (X[i+1][0]-X[i][0])/(3*h[i])
    d.append(temp)

def intv(pt, x):
    for i in range(len(x)-1):
        if(pt>=x[i] and pt<x[i+1]): return i

def evl(pt, x, a, b, X, d):
    i = intv(pt, x)
    return a[i]+b[i]*(pt-x[i])+X[i][0]*pow(pt-x[i], 2)+d[i]*pow(pt-x[i], 3)

pt1 = evl(0.1, x, a, b, X, d)
pt2 = evl(0.3, x, a, b, X, d)
pt3 = evl(0.5, x, a, b, X, d)

print(pt1, pt2, pt3)

print(pt1-f(0.1), pt2-f(0.3), pt3-f(0.5))