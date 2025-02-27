from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:5] if c.isalpha()]
    perms = set((''.join(p) for p in permutations(letters * 2, 3) if p[0] == p[2]))
    return {p for p in perms if len(p) >= 3}