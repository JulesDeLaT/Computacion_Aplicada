import numpy as np
import sys

# Reading number of unknowns
n = 3

k = 0
k1 = 1
k2 = 2

# Making numpy array of n size and initializing 
# to zero for storing solution vector
x = np.zeros

# Reading augmented matrix coefficients
a = [[0.25,0.15,0,1.5],[0.45,0.5,0.75,5],[0.3,0.35,0.25,3]]
        
Det=np.zeros((n,n))
for i in range(n):
    for j in range(n):
        Det[i][j] = a[i][j]
delta = np.linalg.det(Det)

Dk = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        if j==k:
            Dk[i][j] = a[i][n]
        else:
            Dk[i][j] = a[i][j]
delta_1 = np.linalg.det(Dk)

Dk1 = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        if j==k1:
            Dk1[i][j] = a[i][n]
        else:
            Dk1[i][j] = a[i][j]
delta_2 = np.linalg.det(Dk1)

Dk2 = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        if j==k2:
            Dk2[i][j] = a[i][n]
        else:
            Dk2[i][j] = a[i][j]
delta_3 = np.linalg.det(Dk2)

x1 = delta_1/delta
x2 = delta_2/delta
x3 = delta_3/delta

print("x1 = ", x1)
print("x2 = ", x2)
print("x3 = ", x3)