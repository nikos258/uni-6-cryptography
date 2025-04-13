# 4.4 (44) linear branch number
import ask8

m = 5  # the size of the input and output of the S-box
m_str = str(m)


def sbox(x) -> int: return (x ** 2 + 3) % 32


def calculate_correlation_coefficient(a: int, b: int, s_box) -> int:
    """
    Calculates the correlation coefficient of the S-box given the parameters a and b.
    :param a: the first parameter
    :param b: the second parameter
    :param s_box: the S-box passed as the name of a function
    :return: the correlation coefficient
    """
    sum1 = 0
    for x in range(2**m):
        exponent = ask8.xor(format(b*s_box(x), '0'+str(2*m)+'b'), format(a*x, '0'+str(2*m)+'b'))
        if exponent[-1] == '0':  # exponent of (-1) is even
            sum1 += 1
        else:  # exponent of (-1) is odd
            sum1 -= 1
    return sum1


def calculate_hamming_weight(bin_number: str) -> int:
    """
    Calculates the Hamming weight of a string of bits (the number of ones in the string).
    :param bin_number: a string of bits
    :return: the Hamming weight
    """
    count_ones = 0
    for bit in bin_number:
        if bit == '1':
            count_ones += 1
    return count_ones


def calculate_lbn(s_box) -> int:
    """
    Calculates the Linear Branch Number of an S-box.
    :param s_box: the S-box passed as the name of a function
    :return: the Linear Branch Number of the S-box
    """
    min1 = 2*m+1
    for a in range(1, 2**m):
        for b in range(1, 2**m):
            if calculate_correlation_coefficient(a, b, s_box) != 0:
                q = calculate_hamming_weight(format(a, '0'+m_str+'b')) + calculate_hamming_weight(format(b, '0'+m_str+'b'))
                if q < min1:
                    min1 = q
    return min1


print("LBN =", calculate_lbn(sbox))
