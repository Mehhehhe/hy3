# find prime numbers
def soe(num):
    if num > 1:
        A = {} # Contain boolean values from 2 to num. {index:boolean}
        for i in range(2, num):
            A[i] = True # initial setting
        print(A)

soe(13)