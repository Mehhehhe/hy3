from format_dictionary import format_dictionary

# find prime numbers
def soe(num):
    if num > 1:
        A = {} # Contain boolean values from 2 to num. {index:boolean}
        for i in range(2, num):
            A[i] = str(True) # initial setting. 1 = True
        return A

print(format_dictionary(soe(13)))