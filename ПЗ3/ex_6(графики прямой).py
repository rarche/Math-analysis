import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-20,20,1000)
plt.plot(x,np.cos(x))
plt.plot(x,2 * np.cos(x-1) + 1)
plt.plot(x,1/3 * np.cos(x+1.5) - 0.5)
plt.show()