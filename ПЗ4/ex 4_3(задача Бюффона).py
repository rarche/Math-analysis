import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,100)

a = range(-5,5,1)
for i in a:
    plt.plot(x, x*0 + 2*i, c = 'b')
fig = plt.figure(1)
ax = fig.gca()
x_1 = [1, 2]
y_1 = [1, 2.5]
ta = np.array([[[ 2,  1],
              [2,   2.5]],
             [[ 1.666,  1],
              [ 1.666,  2]]])
x, y = ta.T

plt.margins(0.05)
plt.plot(x, y, linewidth=2, color='black')
ax.hlines(1, 1, 2)
figure = ax.plot(x_1, y_1 ,c='r')
plt.show()

#игла длиной b будет пересекать линию при следующих условиях:
#1)правая черная вертикальная линия (равная sin(alfa)*b) >= левой черной вертикальной линии (в данном случае равному a-y)