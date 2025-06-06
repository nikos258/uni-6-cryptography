# 7.4 (84)
import math


def fast_exponentiation(b, e, m):
    """
    Performs fast exponentiation of power mod m.
    :param b: base
    :param e: exponent
    :param m: modulo
    :return: b^e mod m
    """
    result = 1
    while e > 0:
        if e % 2 == 1:
            result = (result * b) % m
        e = math.floor(e/2)
        b = (b**2) % m
    return result


# function from the book
def karatsuba(x,y,B):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        m = max(len(str(x)), len(str(y)))
        m2 = m // 2
        a = x // B**(m2)
        b = x % B**(m2)
        c = y // B**(m2)
        d = y % B**(m2)
        z0 = karatsuba(b, d, B)
        z1 = karatsuba((a + b), (c + d), B)
        z2 = karatsuba(a, c, B)
        return (z2 * B ** (2 * m2)) + ((z1 - z2 - z0) * B ** (m2)) + z0


if __name__ == '__main__':
    base = 10
    modulo = 2**107 - 1

    a = fast_exponentiation(2, 1000, modulo)
    b = fast_exponentiation(3, 101, modulo)
    c = fast_exponentiation(5, 47, modulo)

    temp_product = karatsuba(a, b, base)
    product = karatsuba(temp_product, c, base)
    result = product % modulo
    print("The result of the multiplication is:", result, sep='\n')
