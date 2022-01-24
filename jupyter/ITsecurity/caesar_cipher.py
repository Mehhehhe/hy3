alphabet_wheel = {
    "A":0, "B":1, "C":2, "D":3, "E":4,
    "F":5, "G":6, "H":7, "I":8, "J":9,
    "K":10, "L":11, "M":12, "N":13, "O":14,
    "P":15, "Q":16, "R":17, "S":18, "T":19,
    "U":20, "V":21, "W":22, "X":23, "Y":24,
    "Z":25
}

value_wheel = {index:value for index, value in enumerate(alphabet_wheel)}

def caesar_cipher(msg,shift_num=3,mode="encryption"):
    en = []
    de = []
    result = ""
    if mode == "encryption":
        # print("Encrypting ", msg, " with shift : ", shift_num)
        for i in msg:
            en.append(value_wheel.get((alphabet_wheel.get(i)+shift_num)%26))
        for i in en:
            result += str(i)
        return result
    elif mode == "decryption":
        # print("Decrypting ", msg, " with shift : ", shift_num)
        for i in msg:
            de.append(value_wheel.get((alphabet_wheel.get(i)-shift_num)%26))
        for i in de:
            result += str(i)
        return result

msg = "SONWXAJSVODISNA"
letters_of_msg = list(msg.upper())
# print(letters_of_msg)
for i in range(0,26):
    print("Decryption with shifting number :",i," ,",caesar_cipher(letters_of_msg,i,"decryption"))