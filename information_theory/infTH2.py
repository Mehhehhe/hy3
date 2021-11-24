import numpy as np

c = [25,4,22,5,8,3,10,25,5,4,21]
k = 3
m = []
for i in np.arange(0,10,1):
    print(c[i])
    dec = c[i]-k%11
    m.append(dec)
print(m)