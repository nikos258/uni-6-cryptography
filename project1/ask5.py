# 3.3 (27)
import matplotlib.pyplot as plt


def f(x): return (5 * x + 3) % 2**10


def main():
    x0 = 152  # initial integer
    y = x0
    values = list()  # list of the values f(x_i)
    for i in range(1, 151):
        y = f(y)
        values.append(y)

    print("Number of elements in the list: ", values)
    print("Number of unique elements in the list: ", len(list(set(values))))

    fig, ax = plt.subplots(1, 2)
    plt.title = "Frequency histogram"
    ax[0].hist(values)
    ax[0].set_title("10 bins (default)")
    ax[1].hist(values, bins=32)
    ax[1].set_title("32 bins")
    plt.show()


if __name__ == '__main__':
    main()
