Cipher = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plain = "abcdefghijklmnopqrstuvwxyz"

cipher_code = input()

for pl in plain:
    if(pl != 'a'):
        # key += 1
        plain += plain[0]
        plain = plain[1:]
    
    plain_code = ""

    for code in cipher_code:
        plain_code += plain[Cipher.index(code)]
    
    print(plain_code)