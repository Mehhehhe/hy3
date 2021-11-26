import numpy as np
import matplotlib.pyplot as plt
from pylfsr import LFSR
from operator import xor
#initial state
state = [1,1,1,1,1,1,1,1,1,1]
#before cipher
m=[1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]
# Polynomial G1, G2
fpoly = [10,3]
fpoly2 = [9,8,6,3,2]
# Key generator
# LFSR of 2 polynomial with initial state of all 1
L1 = LFSR(initstate=state, fpoly=fpoly)
L2 = LFSR(initstate=state, fpoly=fpoly2)
# MUX
L = [] # store bit shift from L1, L2
Seq = [] # store mux from L and m
# Generating key 
for _ in range(len(m)):
    #print("L1")
    #print(L1.count,L1.state,'',L1.outbit,L1.seq,sep='\t')
    #print("L2")
    #print(L2.count,L2.state,'',L2.outbit,L2.seq,sep='\t')
    L1.next()
    L2.next()
    L.append(xor(L1.outbit,L2.outbit))
# Mux m and key
for i in range(len(m)):
    Seq.append(xor(m[i],L[i]))
# Output sequence
print('-'*50)
print('Output: ',int("".join(str(x) for x  in Seq)))