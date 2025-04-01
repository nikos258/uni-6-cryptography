# 3.11 (36) RC4
import ask4


n = 2**5


def gen_permutation(seed):
    seedlen = len(seed)
    s = [i for i in range(n)]

    j = 0
    for i in range(n):
        j = (j + s[i] + seed[i % seedlen]) % n
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
    return s


def gen_keystream(s, plaintext):
    i = j = 0
    plen = len(plaintext)
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
key = "HOUSE"

message_bits = ask4.encode(message)
key_bits = [int(bit) for bit in ask4.encode(key)]

permutation = gen_permutation(key_bits)
# keystream = gen_keystream(permutation, message)
# print(len(message), len(keystream), sep='\n')
key_stream = "".join(gen_keystream(permutation, message))

print("key stream: ", key_stream)

cipher = ask4.encrypt(key_stream, message_bits)
print("cipher: ", cipher)

decrypted_cipher = ask4.decrypt(key_stream, cipher)
decrypted_ciphertext = ask4.decode(decrypted_cipher)
print(decrypted_ciphertext)




