# P1 * P2 multiply under polynomial x^8 + x^4 + x^3 + x + 1
# P1 = x^6 + x^4 + x^3 = 0010 1100 0
# P2 = x^7 + x^5 + x^4 + x^2 + x = 0101 1011 0 

# Steps :
# 1.Shifting
# 2.XOR

# p1 = 0x26 # from EXAMPLE
# p2 = 0x9E # from EXAMPLE
p1 = 0x58
p2 = 0xB6

product = 0
mask_mod = 0x11B # x^8 + x^4 + x^3 + x + 1 in hex form

print("P1 * P2 : ",bin(p1),bin(p2)," = ??")

for i in range(8):
    product <<= 1
    if product & 0x100: # Check if product is having a carry bit then do reduction
        product ^= mask_mod
    if p2 & 0x80: # Check if p2 has MSB
        product ^= p1 # mask with p1 so it could not go beyond the highest order
    p2 <<= 1

print(bin(product))