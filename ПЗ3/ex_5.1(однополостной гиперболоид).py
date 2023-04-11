import numpy as np
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)
X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
a = 1
b = 1
c = 2
X, Y = np.meshgrid(X, Y)
Z = np.sqrt(X**2 * c**2/a**2 + Y**2 * c**2/b**2 + c**2)
ax.plot_wireframe(X, Y, Z)
show()
