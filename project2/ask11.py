# 10.21 (153) Pollard factorisation
import math


def f(x):
    return (x*x + 1) % N


def pollard_factorisation(x0):
    """
    Implements Pollard's algorithm for factorisation.
    :param x0: initial value
    :return: a non-trivial divisor of the global variable N
    """
    x = x0
    y = x0
    d = 1
    while d == 1 or d == N:
        x = f(x)
        y = f(f(y))
        d = math.gcd(abs(x-y), N)
    return d


if __name__ == '__main__':
    N = 2**257 - 1
    x0 = 4
    divisor = pollard_factorisation(x0)
    print("A non-trivial divisor is:", divisor)
    print("Check that it is correct:", N % divisor == 0)

# x0 = 4 βρήκε το 535006138814359
