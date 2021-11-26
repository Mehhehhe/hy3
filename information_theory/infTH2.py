import numpy as np

# characters as numbers
c = [25,4,22,5,8,3,10,25,5,4,21]
# shifting factor
k = [1,2,3,4,5,6,7,8,9,10,11]
# number storage
m = []

for j in np.arange(0,len(k),1):
    m.append([(c[i]-k[j]%11) for i in np.arange(0,11,1)])
for i in range(len(m)):
    print("shift",k[i],":",m[i])
    