# 9.29 (127)
import random


def fermat_test(n):
    a = random.randint(2, n-1)
    if gcd(n, a) > 1:
        return True
    if a**(n-1) % n == 1:
        return False
    return True


def gcd(x, y):
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
