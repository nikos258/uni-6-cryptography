# 10.1 (136) trial division


def trial_division(n: int):
    """
    Performs trial division on a positive integer.
    :param n: a positive integer
    :return: a list of all the prime divisors (and the multiplicity of each)
    """
    L = list()
    while n % 2 == 0:
        L.append(2)
        n = n / 2

    f = 3
    while f**2 <= n:
        if n % f == 0:
            L.append(f)
            n = n // f  # floor division to avoid problems when dividing very large numbers
        else:
            f = f + 2
    if n != 1:
        L.append(n)
    return L


if __name__ == '__main__':
    print("Prime divisors of")

    n = 2**62-1
    print("2**62-1:", trial_division(n))

    n = 2**102-1
    print("2**102-1:", trial_division(n))
