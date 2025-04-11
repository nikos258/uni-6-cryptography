# 2.2 (19)


def prepare_dictionaries():
    """
    Makes two dictionaries to join the letters of the greek alphabet and numbers 1-24.
    d1 = {'α':1, 'β':2, ...}
    d2 = {1:'α', 2:'β', ...}
    :return: the two dictionaries
    """
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

    return d1, d2


def main():
    letter_num, num_letter = prepare_dictionaries()

    cipher = "οκηθμφδζθγοθχυκχσφθμφμχγ"
    message = ""
    for letter in cipher:
        idx = letter_num[letter] - 3  # subtract f(x0), where x0 is a root of g
        if idx < 1:  # handles the case when the index is not in the range [1, 24]
            message += num_letter[(idx-1) % 24 + 1]
        else:
            message += num_letter[idx]

    print("The original message is:", message, sep='\n')


if __name__ == '__main__':
    main()