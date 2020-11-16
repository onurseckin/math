def comb(x, y):
    res = 0
    if x < y:
        temp = x
        x = y
        y = temp
    res = 1
    j = 1
    i = y + 1
    while i <= x:
        res *= i
        res /= j
        i += 1
        j += 1
    return res


def galton(start, end, n):
    res = 0
    for i in range(start, end + 1):
        res += comb(n, i)
    res = res / (2.0 ** n)
    return res * 100


print(galton(400, 600, 1000))
