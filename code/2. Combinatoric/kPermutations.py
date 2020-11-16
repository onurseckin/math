# The number of sequences of length k
# composed out of n symbols is n power of k
from itertools import product, permutations


for x in product("ab", repeat=4):
    print("".join(x))

for y in permutations("abcde", 2):
    print("".join(y))

# recap

# rule of sum
print(["Alice", "Bob", "Charlie"] + [0, 1, 2, 3, 4])

# rule of product
for p in product(["a", "b", "c"], ["x", "y"]):
    print("".join(p))

# tuples
for p in product("ab", repeat=3):
    print("".join(p))

# permutations
for p in permutations("abcd", 2):
    print("".join(p))
