# Prove  x * (1,4,3,5)(2,2) = (1,3,5,2)(4,4) * x
#      [0 0 0 1 0]   [0 0 1 0 0]
#      [0 1 0 0 0]   [1 0 0 0 0]
# x *  [0 0 0 0 1] = [0 0 0 0 1] * x
#      [0 0 1 0 0]   [0 0 0 1 0]
#      [1 0 0 0 0]   [0 1 0 0 0]
import numpy as np
left_matrix = [
    [0,0,0,1,0],
    [0,1,0,0,0],
    [0,0,0,0,1],
    [0,0,1,0,0],
    [1,0,0,0,0]
]

right_matrix = [
    [0,0,1,0,0],
    [1,0,0,0,0],
    [0,0,0,0,1],
    [0,0,0,1,0],
    [0,1,0,0,0]
]

res,type_res, size_res, unk = np.linalg.lstsq(left_matrix, right_matrix)
# res,type_res, size_res, unk = np.linalg.lstsq(right_matrix,left_matrix)
#print(np.matmul(right_matrix,res))
#print(np.matmul(left_matrix,res))

print(res)