def multiply_ints_as_polynomials(x, y):
	z = 0
	while x != 0:
		if x & 1 == 1:
			z ^= y
		y <<= 1
		x >>= 1
	return z

def number_bits(x):
	nb = 0
	while x != 0:
		nb += 1
		x >>= 1
	return nb

def mod_int_as_polynomial(x, m):
	nbm = number_bits(m)
	while True:
		nbx = number_bits(x) 
		if nbx < nbm:
			return x
		mshift = m << (nbx - nbm)
		x ^= mshift

def gfmult(x, y):
	z = multiply_ints_as_polynomials(x, y)
	m = int('100011011', 2)
	return mod_int_as_polynomial(z, m)

# input: 4x4 matrix
# output: 4x1 matrix
def mix_column(input_mat):
    ss = [[0,0,0,0]] * 4
    for i in range(4):
        ss[0][i] = gfmult(0x02, input_mat[0][i]) ^ gfmult(0x03, input_mat[1][i]) ^ input_mat[2][i] ^ input_mat[3][i]
        ss[1][i] = input_mat[0][i] ^ gfmult(0x02, input_mat[1][i]) ^ gfmult(0x03, input_mat[2][i]) ^ input_mat[3][i]
        ss[2][i] = input_mat[0][i] ^ input_mat[1][i] ^ gfmult(0x02, input_mat[2][i]) ^ gfmult(0x03, input_mat[3][i])
        ss[3][i] = gfmult(0x03, input_mat[0][i])  ^ input_mat[1][i] ^ input_mat[2][i] ^ gfmult(0x02, input_mat[3][i])
    return ss[0]

input_matrix = [
    [0xF9, 0x04, 0xB9, 0x03],
    [0x35, 0xB2, 0xA7, 0x33],
    [0x65, 0xC8, 0x80, 0x80],
    [0x64, 0x83, 0x25, 0x64]
]

new_matrix = []

for i in range(4):
    input_matrix[i] = mix_column(input_matrix)

for i in input_matrix:
    new_matrix.append(list(hex(j) for j in i))

for i in new_matrix:
    print(i)