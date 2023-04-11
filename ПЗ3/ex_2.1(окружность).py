import matplotlib.pyplot as plt
import numpy as np

x = []
x_2 = []
y = []
y_2 = []
for i in range(1000):
    r = 500
    x.append(-i)
    x_2.append(i)
    y.append(np.sqrt(r ** 2 - i ** 2))
    y_2.append(-np.sqrt(r ** 2 - i **2))

plt.figure(figsize = (4, 4))
plt.plot(x,y)
plt.plot(x_2,y)
plt.plot(x,y_2)
plt.plot(x_2,y_2)
plt.xlabel('x')
plt.ylabel('y')
plt.show()