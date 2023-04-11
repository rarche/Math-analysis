import matplotlib.pyplot as plt
import numpy as np

x = []
x_2 = []
y = []
y_2 = []

for i in range(1000):
    a = 500
    b = 1000
    x.append(-i)
    x_2.append(i)
    y.append(np.sqrt(b**2 - (b**2 * i**2 / a**2)))
    y_2.append(-np.sqrt(b**2 - (b**2 * i**2 / a**2)))

plt.plot(x,y)
plt.plot(x_2,y)
plt.plot(x,y_2)
plt.plot(x_2,y_2)
plt.xlabel('x')
plt.ylabel('y')
plt.show()