import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
def f(x):
    return (np.sin(x*a))

x = np.linspace(100,500,1000)
a = np.arange(0.01,0.02,1000)
plt.plot(x, f(x))
plt.plot([100,500],[0,0],c='r')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

x_0 = fsolve(f,200)
print(x_0)
