# Correction Code 1 HW 2

n = 15 # total bit
k = 8 # initial data size
# From summing of n choose i less than or equal to 2 power of n minus k
# We will get n choose i until i equal to t
# For each terms, ratio are (n-t)/(t+1) which may be less or more than 1 but not negative
# Using summing formula, we will get (1)/(1 - (n-t)/(t+1)) less than or equal to t
# After that, we will see in form of below equation.
equation = ((2**(n-k))*(n-k)+1)/((2**(n-k))-1)
# find ability to correct bit (t)
print("Result (t) must less than or equal : ",equation)