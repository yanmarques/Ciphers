# -*- coding: UTF-8 -*-

import string

# Alphabet list
ALPHA = list(string.ascii_letters)

class CaesarCipher(object):
    def __init__(self, key):
        if key not in ALPHA:
            raise Exception('Key must be a valid alphabet character.')

        self.__key = key
        self.__index = ALPHA.index(key)

    def encrypt(self, text):
        """Encrypt data using old cesar cipher"""

        crypted = []
        text = text.replace(' ', '')

        for letter in text:
            index = (ALPHA.index(letter) - self.__index)
            crypted.append(ALPHA[index])

        return "".join([e for i, e in enumerate(crypted)])

    def decrypt(self, ciphertext):
        """Decrypt data using cesar cipher"""
        
        decrypted = []

        for letter in ciphertext:
            index = ALPHA.index(letter) + self.__index
        
            if index > (len(ALPHA) - 1):
                index = index - len(ALPHA)

            decrypted.append(ALPHA[index])

        return "".join([e for i, e in enumerate(decrypted)])

if __name__ == '__main__':
    caesarCipher = CaesarCipher('f')
    ciphertext = caesarCipher.encrypt('mypasswordz')
    print(ciphertext)
    print(caesarCipher.decrypt(ciphertext))
