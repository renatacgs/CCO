x = [1950, 1960, 1970, 1980, 1991, 2000, 2010, 2020]
y = [55, 88, 125, 241, 367, 501, 604, 699]
n = 8

x1 = sum(x)
x2 = sum(map(lambda x: x ** 2, x))
x3 = sum(map(lambda x: x ** 3, x))
x4 = sum(map(lambda x: x ** 4, x))

y1 = sum(y)
xy = sum(map(lambda x: x[0] * x[1], zip(x, y)))
x2y = sum(map(lambda x: (x[0] ** 2) * x[1], zip(x, y)))

A = [[n, x1, x2],
    [x1, x2, x3],
    [x2, x3, x4]]

R = [y1, xy, x2y]


print(A)
print(R)
