# 4.3 (44) differential uniformity

table = [[0, 2, 3, 7, 9, 12, 15, 7, 6, 15, 15, 1, 7, 3, 1, 0],
         [1, 5, 6, 13, 4, 1, 5, 11, 7, 8, 7, 1, 1, 3, 2, 13],
         [5, 3, 5, 12, 11, 1, 1, 5, 13, 0, 15, 7, 2, 2, 13, 0],
         [3, 12, 3, 11, 2, 2, 2, 4, 6, 5, 5, 0, 4, 3, 1, 0]]

n = 6
m = 4


# calculates the quantity (a xor b)
def xor(a, b):
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result


# calculates the output of an S-box according to the table
def sbox(i):
    row = int(i[0] + i[-1], 2)
    col = int(i[1:n - 1], 2)
    return format(table[row][col], '0' + str(m) + 'b')


def main():
    diff = -1
    for x in range(1, 2 ** n):
        x1 = format(x, '0' + str(n) + 'b')  # converts to a string of the binary number
        for y in range(2 ** m):
            y1 = format(y, '0' + str(m) + 'b')

            cardinality = 0  # the cardinality of the set
            for z in range(2 ** n):
                z1 = format(z, '0' + str(n) + 'b')
                result = xor(sbox(xor(z1, x1)), sbox(z1))
                if result == y1:
                    cardinality += 1
            if cardinality > diff:  # finds the maximum of the cardinalities
                diff = cardinality

    print('The differential uniformity is', diff)


if __name__ == '__main__':
    main()
