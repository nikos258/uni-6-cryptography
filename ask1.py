import math
import numpy as np


g = np.poly1d([1, 3, 1])

f = np.poly1d([1, 3, 3, 7, 5, 4])

d1 = dict()
d2 = dict()
n = ord('α')
for i in range(17):
    d1[chr(n)] = i+1
    d2[i+1] = chr(n)
    n += 1

n += 1
for i in range(17, 24):
    d1[chr(n)] = i+1
    d2[i+1] = chr(n)
    n += 1

cipher = "οκηθμφδζθγοθχυκχσφθμφμχγ"
message = ""
for letter in cipher:
    idx = d1[letter] - 3
    if idx < 1:
        message += d2[(idx-1) % 24 +1]
    else:
        message += d2[idx]

print(message)
# print(d1, d2, sep="\n")
