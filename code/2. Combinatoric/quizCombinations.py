n = 10
count = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i < j and j < k:
                count += 1

# optimized

input = 10


def res(n):
    ans = 0
    n = n - 2
    for i in range(n, 0, -1):
        ans = ans + (i * (i + 1)) / 2
    return ans


print(res(input))
