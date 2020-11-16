from itertools import combinations

count = 0
for a in combinations(["A1 ", "A2 ", "A3 ", "A4 ", "A5 ", "A6 ", "A7 "], 3):
    for b in combinations(["B1 ", "B2 ", "B3 ", "B4 ", "B5 "], 3):
        c = a + b
        count += 1
        print("".join(c))