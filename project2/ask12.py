# 11.3 (163)
from ask11 import pollard_factorisation
import egcd


if __name__ == '__main__':
    C = (3203, 909, 3143, 5255, 5343, 3203, 909, 9958, 5278, 5343, 9958, 5278, 4674,
         909, 9958, 792, 909, 4132, 3143, 9958, 3203, 5343, 792, 3143, 4443)
    N = 11413
    e = 19

    p = pollard_factorisation(2, N)
    q = N // p
    phi = (p-1)*(q-1)
    _, d, _ = egcd.egcd(e, phi)  # find the inverse of e (mod phi)
    M = tuple(pow(block, d, N) for block in C)
    plaintext = ''.join(chr(block) for block in M)
    print(plaintext)

    # print(f"p={p}\nq={q}\nN={p*q}\nphi={phi}\nd={d}")
