from caesar_cipher import alphabet_wheel, value_wheel

def __egcd(a, n):
    r2, r = abs(a), abs(n)
    x, x2, y, y2 = 0, 1, 1, 0
    while r:
        r2, (q, r) = r, divmod(r2, r)
        x, x2 = x2 - q*x, x
        y, y2 = y2 - q*y, y
    return r2, x2 * (-1 if a < 0 else 1), y2 * (-1 if n < 0 else 1)
 
def __modinv(a, n):
	g, x, y = __egcd(a, n)
	if g != 1:
		return None
	return x % n

def affine_cipher(msg, key_a, key_b, mode="encryption"):
    en = []
    de = []
    result = []
    final_result = ""
    if mode == "encryption":
        for i in msg:
            en.append(alphabet_wheel.get(i))
        for i in en:
            result.append(value_wheel.get((((key_a*i)+key_b)%26)))
        for i in result:
            final_result += str(i)
    elif mode == "decryption":
        for i in msg:
            de.append(alphabet_wheel.get(i))
        for i in de:
            result.append(value_wheel.get((((__modinv(key_a, 26)*i)-key_b)%26)))
        for i in result:
            final_result += str(i)
            
    return final_result

original_message = "SONWXAJSVODISNA"
msg_letters = list(original_message)
# print(msg_letters)
for a in range(0,26):
    for b in range(0,26): 
        try:
            print("Alpha : ",a,", Beta : ",b,", Decryption Result : ",affine_cipher(msg_letters, a, b, "decryption"))
        except Exception:
            continue