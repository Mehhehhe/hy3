import math
from Crypto.Cipher import AES
from binascii import hexlify

# information block

inf_block_1 = b'0000000000000000'
inf_block_2 = b'0000000000000001'

# Key 128 bits
key = b'0000000000000000'

# Problems
# 1: Find entropy of cipher of both blocks
# 2: Find code distance of both

# Create a dictionary of hex symbols
def symdict_create(ciphered):
    temp_dict = {"length":len(ciphered)}
    count = 0
    # print("List enumerate ciphered: ",list(enumerate(ciphered)))
    for i in ciphered:
        if i not in temp_dict:
            temp_dict.update({i:1})
            continue
        else:
            temp_dict.update({i:temp_dict.get(i)+1})
    # for index, value in enumerate(ciphered):
    #     if value not in temp_dict:
    #         temp_dict.update({value:{index:1}})
    #         continue
    #     else:
    #         temp_dict.update({value:{}})
    return temp_dict

def symdict_probdec(symdict):
    for i in symdict:
        if i != "length":
            symdict.update({i:(symdict.get(i)/symdict.get("length"))})
    return symdict

def prob_mult_log(prob):
    res = (prob)*math.log(prob)
    return res

def entropy(block):
    sum = 0
    for i in block:
        if i != "" and i != "length":
            sum = sum + prob_mult_log(block.get(i))
    return -sum

def efficiency(entropy, original_msg):
    size = len(original_msg)
    

# Cipher
cipher = AES.new(key, AES.MODE_ECB)

c1 = cipher.encrypt(inf_block_1)
c1_hex = c1.hex()
cc1 = [c1_hex[i:i+2] for i in range(0,len(c1_hex),2)]

c2 = cipher.encrypt(inf_block_2)
c2_hex = c2.hex()
cc2 = [c2_hex[i:i+2] for i in range(0,len(c2_hex),2)]

# Probablity dictionary
cc1_prob = symdict_probdec(symdict_create(cc1))
cc2_prob = symdict_probdec(symdict_create(cc2))

# print("CC1 prob: ",cc1_prob, ", CC2 prob: ", cc2_prob)

# Entropy of cipher
cc1_entropy = entropy(cc1_prob)
cc2_entropy = entropy(cc2_prob)
print("Block 1 entropy: ",cc1_entropy, "\nBlock 2 entropy: ",cc2_entropy)

# 
# Code Distance
# 

L1 = list(inf_block_1)
L2 = list(inf_block_2)
comp = [L1,L2]
count = 0

for i in range(0,int((len(L1)+len(L2))/2)):
    if comp[0][i] != comp[1][i]:
        count = count + 1

print("Hamming distance: ",count)