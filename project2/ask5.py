# 8.50 (106)
import math
import numpy as np


def sum_of_factors_odd(n):
    """
    Calculates the sum of the factors of an odd number greater or equal to 3.
    :param n: an odd number greater or equal to 3
    :return: the sum of all the factors of the number
    """
    limit = n // 3
    sum1 = 1 + n
    for i in range(3, limit+1, 2):
        if n % i == 0:
            sum1 += i
    return sum1


if __name__ == '__main__':
    var1 = math.exp(np.euler_gamma) / 2  # e^gamma / 2

    for n in range(3, 2**20, 2):
        var2 = math.log(math.log(n))  # ln(ln(n))
        if sum_of_factors_odd(n)/n >= var1 * var2 + 0.74 / var2:
            print("Problem!", n, sum_of_factors_odd(n)/n, var1*var2 + 0.74 / var2)

