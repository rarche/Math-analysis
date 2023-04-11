import numpy as np

a = int(input('Input 1-st coordinat: '))
b = int(input('Input 2-nd coordinat: '))
c = int(input('Input 3-rd coordinat: '))
len_of_vector = (a**2 + b**2 + c**2)**0.5
print(f'lenght of vector is {len_of_vector}')

#alternative version
ls = np.array([a, b, c])
n =np.linalg.norm(ls)  #возвращает норму матрицы/вектора
print(n)
