import matplotlib.pyplot as plt
import numpy as np

circle = np.arange(0, 2*np.pi, 1/180)
line = np.arange(1,10,6)
plt.polar(circle, [10]*len(circle))
plt.polar(line)
plt.show()
