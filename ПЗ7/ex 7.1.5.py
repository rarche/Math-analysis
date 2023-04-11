import numpy as np
import matplotlib.pyplot as plt

a = np.array([1,5,0], float)
b = np.array([2,8,7], float)
c = np.array([7,1.5,3], float)
Z = np.cross(a,b)
print(np.inner(Z,c))
