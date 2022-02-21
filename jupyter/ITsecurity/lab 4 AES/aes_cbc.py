import random
from Crypto.Cipher import AES
from os import urandom

# AES CBC
# Problems:
# 1.Find impact of decrypt plaintext if error @ block1 with number of error bit equal to 1
# 2.Same as (1) but 2 bits

# Key 128 bits
key = b'0000000000000000'

# Information of 1 block
block1 = b'0000000000000000'
testblock = b'1234567890123456'

# Random
iv = urandom(16)

# Cipher: Encryption
cipher = AES.new(key, AES.MODE_CBC, iv)
c = cipher.encrypt(block1)
c_hex = c.hex()
cc1 = [c_hex[i:i+2] for i in range(0,len(c_hex),2)]
# print("Before: ",cc1)

# Perform bit flipping attack (randomly) at IV
# May error if it is single hex number, 0-F
iv_hex = iv.hex()
iv1 = [iv_hex[i:i+2] for i in range(0,len(iv_hex),2)]

##   Create random position
# Attack 1 bit
rand_pos = int(random.random()*10)
iv1[rand_pos] = hex(int(iv1[rand_pos], 16) ^ (random.randrange(0,255))).strip("0x")
# print("After replace @[",rand_pos,"] replace with: ",iv1[rand_pos],iv1)

# Comment 2 lines below for problem 1
# # Attack another one bit
rand_pos = int(random.random()*10)
iv1[rand_pos+1] = hex(int(iv1[rand_pos], 16) ^ (random.randrange(0,255))).strip("0x")
# print("After replace @[",rand_pos,"] replace with: ",iv1[rand_pos],iv1)

temp = ""
for i in iv1:
    temp = temp + str(i)
iv = bytes.fromhex(temp)

# Decipher: Decryption
decipher = AES.new(key, AES.MODE_CBC, iv)
msg = decipher.decrypt(c)

print("original message: ",block1,"\nencrypted message: ",c,"\ndecrypted message: ",msg)