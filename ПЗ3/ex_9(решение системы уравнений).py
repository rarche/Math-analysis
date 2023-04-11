import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
def solution(root):
    x, y = root
    return (x**2 - 1 - y, np.exp(x) + x*(1-y) - 1)

x = np.linspace(-10,10,1000)
plt.plot(x, (np.exp(x)+x - 1)/x)
plt.plot(x, x**2 - 1)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-10,10)
plt.grid(True)
plt.show()
x_1,y_1 = fsolve(solution, (2,4))
x_2,y_2 = fsolve(solution, (-1,1))
x_3,y_3 = fsolve(solution, (4,3))
print(x_1, y_1)
print(x_2, y_2)
print(x_3, y_3)