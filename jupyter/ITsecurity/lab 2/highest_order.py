from math import gcd
S = [1,2,3,4,5,6,7]

highest_order = len(S)
perm_orders = range(1,highest_order+1)
res = 0
res_arr = {}

def lcm(array, index):
    if(index == len(array) -1):
        return array[index]
    a = array[index]
    b = lcm(array, index+1)
    return int(abs(a*b) / gcd(a,b))

for i in range(1, highest_order):
    for j in perm_orders:
        if (i+j == highest_order):
            res = i + j
            res_arr.update({i:{"orders":[i,j],"LCM":lcm([i,j],0)}})
            res = 0
        else:
            for k in perm_orders:
                if(i+j+k == highest_order):
                    res = i + j + k
                    res_arr.update({i+30:{"orders":[i,j,k],"LCM":lcm([i,j,k],0)}})
                    res = 0
                else:
                    for l in perm_orders:
                        if (i+j+k+l == highest_order):
                            res = i + j + k + l
                            res_arr.update({i+40:{"orders":[i,j,k,l],"LCM":lcm([i,j,k,l],0)}})
                            res = 0
                        else:
                            for m in perm_orders:
                                if (i+j+k+l+m == highest_order):
                                    res = i + j + k + l +m
                                    res_arr.update({i+50:{"orders":[i,j,k,l,m],"LCM":lcm([i,j,k,l,m],0)}})
                                    res = 0
                                else:
                                    for n in perm_orders:
                                        if (i+j+k+l+m+n == highest_order):
                                            res = i + j + k + l +m + n
                                            res_arr.update({i+60:{"orders":[i,j,k,l,m,n],"LCM":lcm([i,j,k,l,m,n],0)}})
                                            res = 0
                                        else:
                                            for o in perm_orders:
                                                if (i+j+k+l+m+n+o == highest_order):
                                                    res = i + j + k + l +m + n +o
                                                    res_arr.update({i+70:{"orders":[i,j,k,l,m,n,o],"LCM":lcm([i,j,k,l,m,n,o],0)}})
                                                    res = 0
                    

# print(res_arr.items())
pivot = 0
for index,(idx,value) in enumerate(res_arr.items()):
    if index == 0:
        pivot = value.get("LCM")
    if index > 1 and pivot < value.get("LCM"):
        pivot = value.get("LCM")
print(pivot)