# 9.44 (130) Strong pseudoprime base 32
import sympy  # pip install sympy


if __name__ == '__main__':
    a = 32
    n = 3
    found = False
    while not found:  # iterate through the odd numbers
        if not sympy.isprime(n):  # if the number is composite
            s = 1
            while (n-1) % 2**s == 0:  # finds the number s
                s += 1
            s -= 1
            t = (n-1) / 2**s

            if t % 1 == 0:  # if t is an integer
                t = int(t)
                if a**t % n == 1:  # if the first condition is met then stop the program
                    print(f"The smallest strong pseudoprime base 32 is: {n}")
                    break

                for i in range(s):
                    if int((a**t))**(2**i) % n == n-1:  # if the second condition is met then stop the program
                        print(f"The smallest strong pseudoprime base 32 is: {n}")
                        found = True

        n += 2
