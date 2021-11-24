m2c = {
    "A":"S", "B":"N", "C":"P", "D":"U", "E":"J",
    "F":"C", "G":"M", "H":"G", "I":"O", "J":"V",
    "K":"L", "L":"Z", "M":"W", "N":"H", "O":"K",
    "P":"X", "Q":"F", "R":"D", "S":"A", "T":"B",
    "U":"R", "V":"I", "W":"T", "X":"Q", "Y":"E",
    "Z":"Y"
}
sum_count = 0
sum = 0
start_text = ["S","E","C","R","E","T"]
cipher_text = []
temp_text = []

# substitution and append into array for the first time
for i in range(len(start_text)):
    cipher_text.append(m2c.get(start_text[i]))
    temp_text = cipher_text.copy()
sum_count = sum_count + 1
while True:
    if cipher_text == start_text:
        print("EQUAL!")
        print("ROUNDS : "+str(sum_count))
        break
    cipher_text.clear()

    for i in range(len(start_text)):
        cipher_text.append(m2c.get(temp_text[i]))
    temp_text = cipher_text.copy()
    print("CIPHER : "+str(cipher_text))
    sum_count = sum_count + 1