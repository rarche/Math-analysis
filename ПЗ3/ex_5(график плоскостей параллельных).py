from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)
X = np.arange(-10,10,1)
Y = np.arange(-10,10,1)
X,Y = np.meshgrid(X,Y)
Z = X + Y
Z_2 = X + Y + 20
ax.plot_wireframe(X,Y,Z)
ax.plot_wireframe(X,Y,Z_2)
show()