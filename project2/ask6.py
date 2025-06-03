# 8.76 (111)
import time
from concurrent.futures import ProcessPoolExecutor


def sum_of_proper_divisors(n):
    """
    Calculates the sum of all the proper divisors of a positive integer.
    :param n: a positive integer
    :return: the sum of the proper divisors
    """
    limit = n // 2
    sum1 = 1
    for i in range(2, limit+1, 1):
        if n % i == 0:
            sum1 += i
    return sum1


def is_perfect(n):
    """
    Checks if a number is perfect by comparing it with the sum of its proper divisors.
    :param n: a positive integer
    :return: True if the number is perfect, False otherwise
    """
    return n == sum_of_proper_divisors(n)


def main():
    found = False
    n = 8130
    size = 1_000_000

    start = time.time()
    while not found:
        print("Entering", n, end=' ')
        numbers = tuple(i for i in range(n, n + size + 1, 2))
        with ProcessPoolExecutor() as executor:
            results = executor.map(is_perfect, numbers)

        stop = time.time()
        print(f"exiting {(stop - start) / 60} minutes")

        results = zip(numbers, results)
        for result in results:
            if result[1]:
                stop = time.time()
                found = True
                print("Next perfect number:", result[0])
                print(f"It took {(stop - start) / 60} minutes")

        n += size + 2


def lucas_lehmer(p):
    """
    Implements the Lucas-Lehmer algorithm for the primality of Mp, that is the Mersenne number for the odd prime p
    (Mp = 2^p - 1).
    :param p: an odd prime
    :return: True if 2^p - 1 is prime, otherwise False
    """
    s = 4
    M = 2**p - 1
    for _ in range(p-2):
        s = (s*s - 2) % M
    if s == 0:
        return True
    return False


def main2():
    primes = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)  # a tuple with some consecutive primes

    start = time.time()
    for p in primes:
        M = 2 ** p - 1
        if lucas_lehmer(p) and M > 8128:
            M = 2**p - 1
            print("The next perfect number is",  2**(p-1)*M, "for p =", p)
            stop = time.time()
            print(f"It took {stop-start} seconds.")
            break


if __name__ == '__main__':
    main2()
    