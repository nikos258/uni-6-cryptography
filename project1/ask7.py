# 3.11 (36) RC4
import ask4


n = 2**5


def gen_permutation(seed: list[int]) -> list[int]:
    """
    Generates the permutation s for the RC4 cryptography algorithm.
    :param seed: a list with 40 up to 256 bits
    :return: the initial permutation s
    """
    seedlen = len(seed)
    s = [i for i in range(n)]

    j = 0
    for i in range(n):
        j = (j + s[i] + seed[i % seedlen]) % n
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
    return s


def gen_keystream(s, plen):
    """
    Generates the keystream for the RC4 cryptography algorithm.
    :param s: the initial permutation
    :param plen:
    :return: the whole keystream
    """
    i = j = 0

    k = []
    while plen > 0:
        i = (i + 1) % n
        j = (j + s[i]) % n
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        k.append(format(s[(s[i]+s[j]) % n], '05b'))
        plen -= 1
    return k


message = "MISTAKES ARE AS SERIOUS AS THE RESULTS THEY CAUSE".replace(' ', '')
print("message:", message)
key = "HOUSEHOUSE"
print("key:", key)

message_bits = ask4.encode(message)
print("message bits:", message_bits)

key_bits = [int(bit) for bit in ask4.encode(key)]
permutation = gen_permutation(key_bits)

key_stream = "".join(gen_keystream(permutation, len(message)))
print("key stream:", key_stream)

cipher_bits = ask4.encrypt(key_stream, message_bits)
print("cipher bits:", cipher_bits)

ciphertext = ask4.decode(cipher_bits)
print("ciphertext:", ciphertext)

decrypted_cipher = ask4.decrypt(key_stream, cipher_bits)
decrypted_ciphertext = ask4.decode(decrypted_cipher)
print("decrypted ciphertext:", decrypted_ciphertext)
