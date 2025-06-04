# 10.20 (153) Pollard rho algorithm


def f(x, a, b):
    """
    A randomizing function to be used by the Pollard rho algorithm.
    """
    if x < p/3:
        return (g*x) % p, (a+1) % n, b
    elif x < 2*p/3:
        return (x*x) % p, (2*a) % n, (2*b) % n
    else:
        return (h*x) % p, a, (b+1) % n


def pollard_rho_disc_log(x0, m):
    """
    Implements the Pollard rho algorithm for discrete logarithms. Essentially it uses Floyd's cyclical algorithm to
    find collisions. Because of the non-deterministic nature the function might lead to failure.
    :param x0: initialization parameter
    :param m: number of maximum iterations
    :return: a tuple with the number of iterations and the two pairs of exponents OR None in case of failure
    """
    x = x0
    y = x0
    ai = bi = 0
    aj = bj = 0
    for i in range(1, m):
        x, ai, bi = f(x, ai, bi)
        y, aj, bj = f(*f(y, aj, bj))
        if x == y:
            return i, ai, bi, aj, bj
    return None


if __name__ == '__main__':
    p = 3571
    n = p - 1
    g = 2
    h = 2763

    x0 = 1  # 1 is not in G2
    values = pollard_rho_disc_log(x0, p)
    if values is None:
        print("Failure!")
        exit()
    i, a1, b1, a2, b2 = values

    first = (a2-a1) % n
    second = (b1-b2) % n

    for x in range(1, p):
        left = second*x % n
        right = first % n
        if left == right:
            if pow(g, x, p) == h:
                print("The discrete logarithm of h base g mod p is", x)
                break
