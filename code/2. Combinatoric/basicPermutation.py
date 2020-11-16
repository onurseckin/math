# Here is the code printing all 3-permutations of letters a, b, c, d, e, f.
# Run the code and observe the result for better understanding of permutations.

from itertools import permutations

for p in permutations("abcdef", 3):
    print("".join(p))