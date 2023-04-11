import matplotlib.pyplot as plt
import numpy as np

list_of_sum = []
for i in range(10):
    x = np.random.rand(10)
    sum_x = sum(x)
    list_of_sum.append(sum_x)

columns = 10
n, columns, patches = plt.hist(list_of_sum, columns)
plt.xlabel('summ')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()