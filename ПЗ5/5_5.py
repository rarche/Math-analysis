import numpy as np
import matplotlib.pyplot as plt

n = 100
r = 0.7
x = np.random.rand(n)
y = r*x + (1 - r)*np.random.rand(n)
plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

a = (np.sum(x)*np.sum(y) - n*np.sum(x*y))/(np.sum(x)*np.sum(x) - n*np.sum(x*x))
b = (np.sum(y) - a*np.sum(x))/n

A = np.vstack([x, np.ones(len(x))]).T
a1, b1 = np.linalg.lstsq(A, y)[0]
print(a, b)
print(a1, b1)
c = np.corrcoef(x,y)
C = (np.sum((x - (1/n* sum(x)))*(y - (1/n* sum(y)))))/((np.sum((x - (1/n* sum(x)))**2)*np.sum((y - (1/n* sum(y)))**2))**0.5)
print(f'R посчитан python: {c}')
print(f'R посчитан вручную: {C}')
plt.plot([0, 1], [b, a + b])
plt.show()