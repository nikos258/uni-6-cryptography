# 10.20 (153) Pollard rho algorithm
import egcd, math


def f(x, a, b):
    if x < p/3:
        return (g*x) % p, (a+1) % n, b
    elif x < 2*p/3:
        return (x*x) % p, (2*a) % n, (2*b) % n
    else:
        return (h*x) % p, a, (b+1) % n


# def f(x, a, b):
#     if x % 3 == 0:
#         return (x*x) % p, (2*a) % n, (2*b) % n
#     if x % 3 == 1:
#         return (g*x) % p, (a+1) % n, b
#     if x % 3 == 2:
#         return (h*x) % p, a, (b+1) % n


def floyd(x0, m):
    x = x0
    y = x0
    a1 = b1 = 0
    a2 = b2 = 0
    for i in range(1, m):
        x, a1, b1 = f(x, a1, b1)
        y, a2, b2 = f(*f(y, a2, b2))
        # print(i, x, a1, b1, y, a2, b2)
        first = a1 - a2
        second = b2 - b1
        if x == y:
            print(f"first: {first}, second: {second}")
            return i, a1, b1, a2, b2
    return None


if __name__ == '__main__':
    p = 3571
    n = p - 1
    g = 2
    h = 2763

    x0 = 1  # 1 is not in G2
    values = floyd(x0, p)
    i, a1, b1, a2, b2 = values
    print(values)

    first = a1-a2
    second = (b2-b1) % n

    print(f"first: {first}, second: {second}")

    gcd = egcd.egcd(second, n)
    if first % gcd[0] == 0:
        inv = egcd.egcd(second, n//gcd[0])
    print("inverse", inv)

    x = (inv[1] * first) % n
    print(x)
    print(pow(g, x, p))  # verification



    # brute force

    # for x in range(1, p):
    #     left = second*x % n
    #     right = first % n
    #     if left == right:
    #         print(left, right)
    #         print("x", x)
    #         if (g**x) % p == h:
    #             print("bhdgvldfguaiiirfberh")
    #             break
    #         print((g**x) % p, end='\n\n')



