from format_dictionary import format_dictionary
import math
# find prime numbers
def soe(num):
    A = {} # Contain boolean values from 2 to num. {index:boolean}
    if num > 1:    
        for i in range(2, num):
            A[i] = str(True) # initial setting. 1 = True
        limit = math.sqrt(num)
        i = 2
        while i < limit:
            if A[i] == 'True':
                j = i**2
                while j < num:
                    A[j] = str(False)
                    j = j + i
            i = i + 1
    dict_length = len(A)
    i = 0
    while i <= dict_length+1:
        A.pop(i) if A.get(i) == "False" else ""
        i = i + 1
    return A

print(format_dictionary(soe(30)))