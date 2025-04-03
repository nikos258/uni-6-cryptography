# 4.4 (44) linear branch number
import ask8

m = 5
m_str = str(m)


def sbox(x): return (x ** 2 + 3) % 32


def calculate_correlation_coefficient(a, b):
    sum1 = 0
    for x in range(2**m):
        exponent = ask8.xor(format(b*sbox(x), '0'+str(2*m)+'b'), format(a*x, '0'+str(2*m)+'b'))
        if exponent[-1] == '0':  # exponent is even
            sum1 += 1
        else:
            sum1 -= 1
    return sum1


def calculate_hamming_weight(bin_number):
    count_ones = 0
    for bit in bin_number:
        if bit == '1':
            count_ones += 1
    return count_ones


def calculate_lbn():
    min1 = 2*m+1
    for a in range(1, 2**m):
        for b in range(1, 2**m):
            if calculate_correlation_coefficient(a, b) != 0:
                q = calculate_hamming_weight(format(a, '0'+m_str+'b')) + calculate_hamming_weight(format(b, '0'+m_str+'b'))
                if q < min1:
                    min1 = q
    return min1


print("LBN: ", calculate_lbn())
