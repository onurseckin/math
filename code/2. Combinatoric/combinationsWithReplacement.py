from itertools import combinations_with_replacement

count = 0
for c in combinations_with_replacement("TBL", 4):
    count += 1
    print("".join(c))
print(count)