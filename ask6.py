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


ab = "ab".upper()
encoded_ab = ask4.encode(ab)

sq = "sq".upper()
encoded_sq = ask4.encode(sq)

seed = ""
for i in range(len(encoded_ab)):
    seed += ask4.xor(encoded_ab[i], encoded_sq[i])


print("seed  ", seed[::-1])

cipher = "i!))aiszwykqnfcyc!?secnncvch".upper()
encoded_cipher = ask4.encode(cipher)

seed = [int(bit) for bit in seed][::-1]  # yes reversed


key_stream = lfsr(seed, [0, 0, 0, 0, 0, 1, 1, 0, 1, 1], len(encoded_cipher)+10, 1)
# print(key_stream)

key = ""
for bit in key_stream:
    key += str(bit)

binary_message = ask4.encrypt(key[10:], encoded_cipher)
message = ask4.decode(binary_message)
print(message)
