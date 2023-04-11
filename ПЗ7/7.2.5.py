from pylab import *
from mpl_toolkits.mplot3d import Axes3D

def Q(x,y,z):
    return (x**2 + y**2 + z**2)

fig = figure()
ax = Axes3D(fig)
X = np.arange(-50,50,1)
Y = np.arange(-50,50,1)
X,Y = np.meshgrid(X,Y)
xlabel('X')
ylabel('Y')

ax.plot_surface(X,Y,Q(X,(10*X - 14),(21*X - 29)))
plt.show()

A = np.array([[1, 2, -1], [8, -5, 2]])
B = np.array([1, 12])
print(np.linalg.lstsq(A, B))