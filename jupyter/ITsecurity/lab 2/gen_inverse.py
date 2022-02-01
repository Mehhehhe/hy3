# Generate GF(2^8) & find inverse under polynomial
# x^8 + x^4 + x^3 + x^2 + 1

#   reference : https://kidskangla.wordpress.com/2019/06/03/finding-the-inverse-of-x21-modulo-x4x1-using-extended-euclidean-algorithm-in-sagemath-gf24/

from operator import mod
initial = 0x01
s = [['1']]

mask_mod = 0x11D

r1 = list(bin(mask_mod)[2:])

def division(dividend, divisor):
    quotient_list = [0] * len(r1)
    dividend_i = get_degree(dividend)
    divisor_j = get_degree(divisor)
    while (dividend_i >= divisor_j) and ('1' in dividend):
        t_power = dividend_i - divisor_j
        t_coefficient = int(int(dividend[dividend_i])/int(divisor[divisor_j]))
        quotient_list[t_power] = t_coefficient
        t_mul = [0] * len(r1)
        for i in range(0,divisor_j+1):
            # print(i)
            t_mul[i+t_power] = int(divisor[i]) * t_coefficient
        
        for i in range(len(dividend)):
            dividend[i] = mod(int(dividend[i]) - t_mul[i],2)

        dividend_i = get_degree(dividend)
    return quotient_list, dividend

def get_degree(val):
    global deg
    for i in range(len(val)):
        if int(val[i]) != 0:
            deg = int(i)
    return deg

def generate_s(p=initial):
    for i in range(15):
        p <<= 1
        if p & 0x100:   # mask 8 bit
            p &= 0xFF
            p ^= 0x0F
        s.append(list(format(p,'09b')))


generate_s()
s_copy = s

t1 = [0] * len(r1)
t2 = [0] * len(r1)
t2[0] = 1

t = [0] * len(r1)

itr = 1

for i in s:
    # print("Current member : ", i)
    while '1' in i:
        # print('\n'+str(itr))
        # print('Dividend: '+str(r1))
        # print('Divisor : '+str(i))

        quotient, remainder = division(r1,i)
        # print('Quotient : '+str(quotient)+', remainder'+str(remainder))

        t_qt2 = [0] * len(r1)
        degree_quot = get_degree(quotient)
        degree_t2 = get_degree(t2)

        for j in range(degree_quot+1):
            for k in range(degree_t2+1):
                try:
                    t_qt2[j+k] = t_qt2[j+k] + (quotient[j] * t2[k])
                except Exception:
                    continue
        
        for l in range(len(r1)):
            t[l] = mod(t1[l] - t_qt2[l],2)
        
        if get_degree(r1) == get_degree(t):
            # print('perform mod')
            t_quotient, t_remainder = division(t, r1)
            t = list(t_remainder)
        
        r1 = list(i)
        i = list(remainder)
        t1 = list(t2)
        t2 = list(t)
        # print("t1 : ",t1)
        # print("t2 : ",t2)
        # print("t : ",t)
        itr += 1

print("\n\nInverse : ",t1)