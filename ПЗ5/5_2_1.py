import numpy as np

list_red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
z = 0
r = 0
b = 0
n = 0
for i in range(0,100):
    t = int(np.random.uniform(0,36))
    if t==0:
        z += 1
    elif t in list_red:
        r += 1
        n += 1
    else:
        b += 1
        n += 1
p_r = r/100
p_b = b/100
if n/100 == p_r + p_b:
    print(True)
else:
    print(False)
print(p_r,p_b)