import numpy as np

list_red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
for i in range(0,10):
    y = input()
    t = int(np.random.uniform(0,36))
    if t==0:
        print('zero')
    elif t in list_red:
        print('red')
    else:
        print('black')