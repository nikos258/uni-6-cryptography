# 9.29 (127)
import random


def fermat_test(n):
    """
    Implements Fermat's Test of primality
    :param n: a positive integer > 2
    :return: True if the number is composite, False if the number is probably prime
    """
    a = random.randint(2, n-1)
    if gcd(n, a) > 1:
        return True
    if pow(a, n-1, n) == 1:
        return False
    return True


def gcd(x, y):
    """
    Calculates the greatest common divisor of two numbers. The first argument must be greater than or equal to the
    second argument.
    :param x: the larger number
    :param y: the smaller number
    :return: the greatest common divisor
    """
    assert x >= y
    while y != 0:
        t = y
        y = x % t
        x = t
    return x


if __name__ == "__main__":
    n = 3714089895285 * 2**60000 - 1
    print(fermat_test(n))

    n2 = 2*n+1
    print(fermat_test(n2))
