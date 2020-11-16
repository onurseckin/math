C = dict()  # C([n,k]) is equal to n choose k

for n in range(14):
    C[n, 0] = 1
    C[n, n] = 1

    for i in range(1, n):
        C[n, i] = C[n - 1, i - 1] + C[n - 1, i]

print(C[12, 6])
print(C[10, 4])


def binomial(a, b, n):
    res = []
    for k in range(0, n + 1):
        res.append(C[n, k] * pow(a, n - k) * pow(b, k))
    return res


s = binomial(3, -2, 3)
r = ",".join(map(str, s))
print(r)
