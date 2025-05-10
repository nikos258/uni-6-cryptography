# 4.8 (50) avalanche effect on AES-128
from Crypto.Cipher import AES  # pip install pycryptodome
import random

n = 32  # the length of the message in bytes


def prepare_messages():
    """
    Makes two random messages which differ in just one bit. They are delivered in a byte string format.
    :return: two byte strings
    """
    m1 = tuple(random.randint(0, 255) for _ in range(n))  # tuple of random bytes

    # turn the bytes to a string of bits
    temp = ""
    for i in range(n):
        temp += format(m1[i], "08b")

    # change a random bit
    index = random.randint(0, 8*n-1)
    if temp[index] == '0':
        temp = temp[:index] + '1' + temp[index+1:]
    else:
        temp = temp[:index] + '0' + temp[index+1:]

    # turn the string of bits to a list of bytes
    m2 = []
    for i in range(0, 8*n, 8):
        m2.append(int(temp[i:i+8], 2))

    return bytes(m1), bytes(m2)


def process_ciphertexts(c1, c2):
    """
    Turns two byte strings into strings of bits and counts on how many bits they differ.
    :param c1: the first string of bytes
    :param c2: the second string of bytes
    :return: the amount of bits where c1 and c2 differ as a percentage
    """
    c1_bits = ""
    for byte in c1:
        c1_bits += format(byte, "08b")

    c2_bits = ""
    for byte in c2:
        c2_bits += format(byte, "08b")

    count = 0
    for i in range(8*n):
        if c1_bits[i] != c2_bits[i]:
            count += 1
    return count / (8*n)


def avalanche_effect_AES_ECB():
    """
    Tests for the avalanche effect on the AES-128 algorithm with the ECB mode of operation. For a number of iterations
    the function encrypts a pair of messages which differ by one bit, then counts the number of bits the two ciphertexts
    differ on (call it x). It calculates the average of x over those iterations.
    :return: the average difference in the pair of ciphertexts
    """
    iterations = 50
    sum1 = 0
    for i in range(iterations):
        key = bytes(tuple(random.randint(0, 255) for _ in range(16)))  # random key (16 bytes)
        aes_object = AES.new(key=key, mode=AES.MODE_ECB)  # initialization object of AES-128

        m1, m2 = prepare_messages()

        ciphertext1 = aes_object.encrypt(m1)
        ciphertext2 = aes_object.encrypt(m2)

        sum1 += process_ciphertexts(ciphertext1, ciphertext2)

    return sum1 / iterations


def avalanche_effect_AES_CBC():
    """
    Tests for the avalanche effect on the AES-128 algorithm with the CBC mode of operation. For a number of iterations
    the function encrypts a pair of messages which differ by one bit, then counts the number of bits the two ciphertexts
    differ on (call it x). It calculates the average of x over those iterations.
    :return: the average difference in the pair of ciphertexts
    """
    iterations = 50
    sum1 = 0
    for i in range(iterations):
        key = bytes(tuple(random.randint(0, 255) for _ in range(16)))  # random key (16 bytes)
        aes_object = AES.new(key=key, mode=AES.MODE_CBC)  # initialization object of AES-128, the iv is random

        m1, m2 = prepare_messages()

        ciphertext1 = aes_object.encrypt(m1)
        ciphertext2 = aes_object.encrypt(m2)

        sum1 += process_ciphertexts(ciphertext1, ciphertext2)

    return sum1 / iterations


def main():
    print("Avalanche effect")
    print("AES-128 ECB: ", avalanche_effect_AES_ECB())
    print("AES-128 CBC: ", avalanche_effect_AES_CBC())


if __name__ == '__main__':
    main()
