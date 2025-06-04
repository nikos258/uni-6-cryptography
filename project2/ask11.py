# 10.21 (153) Pollard factorisation
import math


def f(x, N):
    return (x*x + 1) % N


def pollard_factorisation(x0, N):
    """
    Implements Pollard's algorithm for factorisation.
    :param x0: initial value
    :param N: the number to factorise
    :return: a non-trivial divisor of the global variable N
    """
    x = x0
    y = x0
    d = 1

    safety_switch = 1  # for breaking the loop in case the number is prime
    while (d == 1 or d == N) and safety_switch < 2*N:
        x = f(x, N)
        y = f(f(y, N), N)
        d = math.gcd(abs(x-y), N)
        safety_switch += 1
    return d


if __name__ == '__main__':
    N = 2**257 - 1
    x0 = 4
    divisor = pollard_factorisation(x0, N)
    print("A non-trivial divisor is:", divisor)
    print("Check that it is correct:", N % divisor == 0)
