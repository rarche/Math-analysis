import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.linalg

A = np.array([  [1,2,3],[4,5,6],[7,8,9]])
B = np.array([2,5,11])
Q,R = np.linalg.qr(A)
R1 = R[:2, :2]
B1 = np.dot(np.transpose(Q), B)[:2]
X_1 = np.linalg.solve(R1,B1)
X = np.append(X_1,0)
print(X)
print(np.linalg.norm(X))

X = np.array([1.5, 1, 0.5])
print(np.linalg.norm(X),  np.linalg.norm(np.dot(A, X) - B))