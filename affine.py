# -*- coding: UTF-8 -*-

import string
import functools

# Alphabet list
ALPHA = list(string.ascii_lowercase)

class AffineCipher(object):
    def __init__(self, a, b):
        if not self.validKey(a):
            raise Exception('Key {} is not valid.'.format(a))
        elif not self.validKey(b):
            raise Exception('Key {} is not valid.'.format(b))

        self.__a = a
        self.__b = b

    # Valid a key verifying if it has no factors in commom with the length of ALPHA
    def validKey(self, key):
        for factor in self.__factors(len(ALPHA)):
            for number in self.__factors(key):
                if number == factor: return False

        return True

    def encrypt(self, text):
        """Encrypt data using affine cipher"""

        crypted = []
        text = text.replace(' ', '').replace('.', '').replace(',', '').lower()

        for letter in text:
            index = (self.__a * ALPHA.index(letter)) + self.__b
            
            while index > (len(ALPHA) - 1):
                index = index - len(ALPHA)

            crypted.append(ALPHA[index])
        
        return "".join([e for i, e in enumerate(crypted)])

    def decrypt(self, ciphertext):
        """Decrypt data using cesar affine cipher"""
        
        decrypted = []

        for letter in ciphertext:
            index = self.__mod(self.__mod_inverse() * (ALPHA.index(letter) - self.__b))
            
            while index > (len(ALPHA) - 1):
                index = index - len(ALPHA)
    
            decrypted.append(ALPHA[index])

        return "".join([e for i, e in enumerate(decrypted)])
    
    # Factors of a number
    def __factors(self, n):
        factors = list(functools.reduce(list.__add__, 
            ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
        
        return [i for i in factors if i != 1]

    # Modular muplicative inverse of key A
    def __mod_inverse(self):
        a = self.__a % len(ALPHA);
        for x in range(1, len(ALPHA)) :
            if ((a * x) % len(ALPHA) == 1) :
                return x
        return 1

    # Module of a number (mod 26)
    def __mod(self, a):
        c = a % len(ALPHA)
        return c + len(ALPHA) if c > 0 else c

if __name__ == '__main__':
    affineCipher = AffineCipher(1, 17)
    ciphertext = affineCipher.encrypt('mypasswordz')
    plain = affineCipher.decrypt(ciphertext)
    print(ciphertext, plain)