# 2.6 (20)
import random

char_to_num = {
    'A': '00000', 'B': '00001', 'C': '00010', 'D': '00011', 'E': '00100',
    'F': '00101', 'G': '00110', 'H': '00111', 'I': '01000', 'J': '01001',
    'K': '01010', 'L': '01011', 'M': '01100', 'N': '01101', 'O': '01110',
    'P': '01111', 'Q': '10000', 'R': '10001', 'S': '10010', 'T': '10011',
    'U': '10100', 'V': '10101', 'W': '10110', 'X': '10111', 'Y': '11000',
    'Z': '11001', '.': '11010', '!': '11011', '?': '11100', '(': '11101',
    ')': '11110', '-': '11111'
}

num_to_char = {
    '00000': 'A', '00001': 'B', '00010': 'C', '00011': 'D', '00100': 'E',
    '00101': 'F', '00110': 'G', '00111': 'H', '01000': 'I', '01001': 'J',
    '01010': 'K', '01011': 'L', '01100': 'M', '01101': 'N', '01110': 'O',
    '01111': 'P', '10000': 'Q', '10001': 'R', '10010': 'S', '10011': 'T',
    '10100': 'U', '10101': 'V', '10110': 'W', '10111': 'X', '11000': 'Y',
    '11001': 'Z', '11010': '.', '11011': '!', '11100': '?', '11101': '(',
    '11110': ')', '11111': '-'
}
# dictionaries made by Chat GPT


def xor(a, b):
    """
    Performs the exclusive or operation on two bits. Supposes that the input is two one-bit strings.
    :param a: the first operand bit
    :param b: the second operand bit
    :return: the result of the expression a xor b
    """
    if a == b:
        return '0'
    return '1'


def produce_key(length):
    """
    Produces a random key to be used for encryption of data. The key is a string of random bits with a given length.
    :param length: the length of the key in bits
    :return: the random key
    """
    bits = ('0', '1')
    key = ""
    for i in range(length):
        key += random.choice(bits)
    return key


def encode(string):
    """
    Encodes a character string to a bit string. The message must consist of characters found in the specific directory.
    :param string: a string of characters
    :return: a string of bits
    """
    encoded = ""
    for letter in string.replace(' ', ''):
        encoded += char_to_num[letter]
    return encoded


def encrypt(key, message):
    """
    Implements the One-Time-Pad crypto-system for encryption of a message.
    :param key: a string of bits, must be of equal length to the message
    :param message: the message represented a string of bits
    :return: the ciphertext
    """
    ciphertext = ""
    length = len(message)
    for i in range(length):
        ciphertext += xor(key[i], message[i])
    return ciphertext


def decrypt(key, ciphertext):
    """
    Implements the One-Time-Pad crypto-system for decryption of a ciphertext.
    :param key: a string of bits, must be of equal length to the ciphertext
    :param ciphertext: a string of bits
    :return: the decrypted bit string
    """
    decrypted = ""
    length = len(ciphertext)
    for i in range(length):
        decrypted += xor(key[i], ciphertext[i])
    return decrypted


def decode(bit_stream):
    """
    Decodes a bit string to a character string. The message must consist of 5-bit blocks
    as found in the specific directory.
    :param bit_stream: a string of 5-bit blocks
    :return: a string of characters
    """
    decoded = ""
    end = 5
    while end <= len(bit_stream):
        decoded += num_to_char[bit_stream[end-5:end]]
        end += 5
    return decoded


def main():
    m = "THESSALONIKI MOU"

    encoded = encode(m)
    print(encoded)

    k = produce_key(len(encoded))
    print(k)

    c = encrypt(k, encoded)
    print(c)

    decrypted = decrypt(k, c)
    print(decrypted)

    received_message = decode(decrypted)
    print(received_message)


if __name__ == '__main__':
    main()
