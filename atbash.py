# -*- coding: UTF-8 -*-

import string

# Alphabet list
ALPHA = list(string.ascii_letters)

def encrypt(text):
    """Encrypt data using old atbash cipher"""

    crypted = []

    text = text.replace(' ', '')

    for iten in text:
        i = 0
        while i < len(iten):
            index = ALPHA.index(iten[i])

            if index == 0:
                crypted.append(ALPHA[len(ALPHA) - 1])
            else:
                crypted.append(ALPHA[index - 1])
            i += 1

    return "".join([e for i, e in enumerate(crypted)])

def decrypt(ciphertext):
    """Decrypt data using atbash cipher"""
    
    decrypted = []
    i = 0
    
    while i < len(ciphertext):
        index = ALPHA.index(ciphertext[i])

        if index == (len(ALPHA) - 1):
            decrypted.append(ALPHA[0])
        else:
            decrypted.append(ALPHA[index + 1])

        i += 1        

    return "".join([e for i, e in enumerate(decrypted)])

if __name__ == '__main__':
    ciphertext = encrypt('myatbashcipher99')
    print(ciphertext)
    print(decrypt(ciphertext))