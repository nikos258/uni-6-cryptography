# 8.76 (111)
import time
from concurrent.futures import ProcessPoolExecutor


def sum_of_proper_divisors(n):
    limit = n // 2
    sum1 = 1
    for i in range(2, limit+1, 1):
        if n % i == 0:
            sum1 += i
    return sum1


def is_perfect(n): return n == sum_of_proper_divisors(n)


if __name__ == '__main__':
    found = False
    n = 2
    size = 1024

    start = time.time()
    while not found:
        numbers = [i for i in range(n, n+size+1, 2)]
        with ProcessPoolExecutor(max_workers=16) as executor:
            results = executor.map(is_perfect, numbers)

        results = zip(numbers, results)
        for result in results:
            if result[1]:
                stop = time.time()
                # found = True
                print("Next perfect number:", result[0])
                print(f"It took {(stop-start)/60} minutes")

        n += size+2
