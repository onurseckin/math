import math


def twentyOne(reach, count, res):
    print(count, res)
    if reach - 1 == res:
        exit()
    res = round((res + reach) / 2)
    count += 1
    twentyOne(reach, count, res)


twentyOne(2097151, 0, 0)
