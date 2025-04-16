# 2.4 (19)
import numpy
import galois  # pip install galois


n = 16  # number of bits of the message
gf = galois.GF(2)

# prepare matrix A
A = numpy.zeros((n, n), dtype=int)
for i in range(n):
    A[i, i] = 1
    A[i, (i+6) % n] = 1
    A[i, (i+10) % n] = 1

A = gf(A)

# check that decryption is correct
for i in range(2**n):
    m = gf(list(format(i, "016b")))
    c = A @ m
    decrypted_c = numpy.linalg.solve(A, c)

    if not numpy.array_equal(m, decrypted_c):
        print("This pair does not match:")
        print("m1 =", m)
        print("m2 =", decrypted_c)
        break
else:
    print("All pairs match.")
