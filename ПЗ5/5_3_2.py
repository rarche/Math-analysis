import numpy as np
from math import factorial as fact
# 3 успеха среди 7 испытаний
k, n = 0, 10000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
e = np.random.randint(0, 2, n)
f = np.random.randint(0, 2, n)
g = np.random.randint(0, 2, n)
x = a + b + c + d + e + f + g

for i in range(0, n):
    if x[i] == 3:
        k = k + 1

C = fact(7)/(fact(3)* fact(4))
P = C/2**7
V = C * 0.5**3 * 0.5**(7-3)
print(P)
print(V)
print(k/n)