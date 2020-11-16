from itertools import combinations

for c in combinations("abc", 2):
    print("".join(c))

# recursion: two teams in n number of teams playing each other in a tournament
# it outputs total number of matches
# n choose 2
def T(n):
    if n <= 1:
        return 0
    return (n - 1) + T(n - 1)


print(T(16))