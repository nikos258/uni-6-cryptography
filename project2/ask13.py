# 12.2 (175) Wiener attack
import math
from fractions import Fraction
import base64


def continued_fraction(x):
    """
    Calculates and returns the continued fraction of a real number.
    :param x: a real number
    :return: [a0;a1,a2,...]=x
    """
    L = list()
    L.append(Fraction(math.floor(x)))
    x = x - L[0]
    while x > 0:
        L.append(Fraction(math.floor(1/x)))
        x = 1/x - L[-1]
    return L


def wiener_attack(N, e):
    """
    Implements Wiener's attack for RSA.
    :param N: RSA number
    :param e: the public exponent
    :return: the secret exponent d
    """
    sequence = continued_fraction(Fraction(e, N))

    fractions = list()
    for i in range(1, len(sequence)):
        temp = 1/sequence[i]
        for j in range(i-1, 0, -1):
            temp += sequence[j]
            temp = 1/temp
        temp += sequence[0]
        fractions.append(temp)

    for fraction in fractions:
        if pow(2, e*fraction.denominator, N) == 2:
            return fraction.denominator
    return None


if __name__ == '__main__':
    N, e = 194749497518847283, 50736902528669041
    d = wiener_attack(N, e)
    print("d =", d)

    with open("extra_files/ciphertext13", 'r') as in_file:
        ciphertext = in_file.read()
        cipher = base64.b64decode(ciphertext).decode('utf-8')
        cipher = cipher.replace('\r\n', ',')[3:-1]  # keep the string of numbers separated with commas

        C = [int(i) for i in cipher.split(',')]  # the list of decoded numbers

        print(''.join(chr(pow(i, d, N)) for i in C))
