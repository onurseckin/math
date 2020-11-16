def divisibleByTwoThree():
    count = 0
    intersection = 0
    for i in range(1000):
        if i % 2 == 0 or i % 3 == 0:
            count = count + 1
    return count


print(divisibleByTwoThree())


def showAll():
    count = 0
    for i in range(1000):
        if i % 2 == 0 or i % 3 == 0:
            print(i)


showAll()