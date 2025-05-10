# 3.8 (34)
import ask4
from collections import deque


def sumxor(l):
    r = 0
    for v in l:
        r = r ^ v
    return r


def lfsr(seed, feedback, bits, flag):
    index_of_ones = []
    feedback_new = []
    for i in range(len(feedback)):
        if 1 in feedback:
            index_of_ones.append(feedback.index(1))
            feedback[feedback.index(1)] = 0
    feedback_new = index_of_ones  # this is a list which contains the positions of 1s in feedback list
    seed = deque(seed)  # make a new deque
    output = []
    if flag == 0:
        print('initial seed :', seed)
    for i in range(bits):
        xor = sumxor([seed[j] for j in feedback_new])
        output.append(seed.pop())  # extract to output the right-most bit of current seed
        seed.appendleft(xor)  # insert from left the result of the previous xor
        if flag == 0:
            print('state', i + 1, 'of the lfsr :', seed)
    return output


# encode the ciphertext
ciphertext = "i!))aiszwykqnfcyc!?secnncvch".upper()
encoded_cipher = ask4.encode(ciphertext)

# encode "ab"
ab = "ab".upper()
encoded_ab = ask4.encode(ab)

# encode "sq"
sq = "sq".upper()
encoded_sq = ask4.encode(sq)

# perform xor on "ab" and "sq" to get the seed
seed = ""
for i in range(len(encoded_ab)):
    seed += ask4.xor(encoded_ab[i], encoded_sq[i])

seed = [int(bit) for bit in seed][::-1]  # make the seed a list of binary integers and reverse it for the lfsr
print("seed:", seed)

# feed the lfsr and get the key stream
key_stream = lfsr(seed=seed, feedback=[0, 0, 0, 0, 0, 1, 1, 0, 1, 1], bits=len(encoded_cipher)+10, flag=1)
print("key stream:", key_stream)

# turn the key stream to string of binary numbers
key = ""
for bit in key_stream:
    key += str(bit)

binary_message = ask4.decrypt(key[10:], encoded_cipher)
message = ask4.decode(binary_message)
print("message:", message.lower())
