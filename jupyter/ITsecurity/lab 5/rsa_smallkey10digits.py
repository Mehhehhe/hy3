# Find the message

N = 1602475129  # Modulus
p=19801
q=80929

# public key
e = 64037

cipher = 1187226754

def eea(a, b):
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s, old_t

def inv(n, p):
    gcd, x, y = eea(n, p)
    assert (n * x + p * y) % p == gcd
    if gcd != 1:
    # Either n is 0, or p is not a prime number.
        raise ValueError(
            '{} has no multiplicative inverse '
            'modulo {}'.format(n, p))
    else:
        return x % p

def phi(a, b):
    return ((a-1)*(b-1))

z = phi(p,q)
d = inv(e,z)
assert(d*e)%z == 1
msg = 1
i = 1

if 1 & d:
    msg = cipher

# Formula => M = C^d mod N
while d:
    d >>= 1 #   Shift right to divide by 2
    
    # Why base squared ever stages?
    # - Example: 3^15 = 3^8 * 3^4 * 3^2 * 3^1
    # First stage:  3^1
    # Stage 2:      3^2 = 3^(1+1) = 3^1 * 3^1
    # Stage 3:      3^4 = 3^(2+2) = 3^2 * 3^2
    # Meaning it's using previous base (in this code: cipher) so until it reaches the final largest exponent,
    # base aka cipher will be squared but also remind that it must not 
    # exceed the maximum size of number set which is N.

    cipher = (cipher * cipher) % N
    
    # result is store if remainder is 1.
    if (d & 1) :msg = (msg * cipher) % N
    i <<= 1 # Just for checking stages.
    
print("Decrypted and get message value: ", msg)