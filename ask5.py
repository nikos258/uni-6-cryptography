import matplotlib.pyplot as plt


def f(x): return (5 * x + 3) % 2**10


x0 = 3
y = x0
values = list()
for i in range(1, 151):
    y = f(y)
    values.append(y)

print(values)

plt.hist(values, bins='auto', normed=True)
plt.show()
