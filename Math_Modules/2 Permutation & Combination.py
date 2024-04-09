from math import factorial

# permutations
def permutations(n, r):
    return factorial(n) // factorial(n - r)

# combinations
def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

n = 5
r = 3
perm_result = permutations(n, r)
comb_result = combinations(n, r)

print(f"The number of permutations of {n} items taken {r} at a time (P({n}, {r})) is: {perm_result}")
print(f"The number of combinations of {n} items taken {r} at a time (C({n}, {r})) is: {comb_result}")
