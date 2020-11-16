from itertools import product

A = ["a", "b"]
B = [1, 2, 3]
resList = list(product(A, B))
print(resList)
print(type(resList[0]))  # each result in the list is tuple
