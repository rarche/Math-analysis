import numpy as np
from math import factorial as fact

k, n = 0, 10000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1
C = fact(4)/(fact(2) * fact(2))
P = C/2**4
V = C * 0.5**2 * 0.5**(4-2)
print(P)
print(V)
print(k/n)