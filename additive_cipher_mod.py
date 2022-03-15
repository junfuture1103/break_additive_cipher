Cipher = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plain = "abcdefghijklmnopqrstuvwxyz"

cipher_code = input()

key = 0

for pl in plain:
    plain_code = ""
    for code in cipher_code:
        plain_code += plain[(Cipher.index(code)+key)%26]
    key += 1
    print(plain_code)