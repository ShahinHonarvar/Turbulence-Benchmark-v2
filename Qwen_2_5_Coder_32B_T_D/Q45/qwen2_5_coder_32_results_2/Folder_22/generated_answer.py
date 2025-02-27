from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:7] if c.isalpha()]
    perms = set(permutations(letters * 2, 3))
    palindromes = {p[0] + p[1] + p[0] for p in perms if p[0] == p[2]}
    return palindromes