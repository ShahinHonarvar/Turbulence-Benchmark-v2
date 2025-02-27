from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:4] if c.isalpha()]
    perms = set(permutations(letters, 3))
    palindromes = {''.join(p) for p in perms if p[0] == p[2]}
    return palindromes