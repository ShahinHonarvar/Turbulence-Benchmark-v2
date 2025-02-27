from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:5] if c.isalpha()]
    perms = set((''.join(p) for p in permutations(letters, 4)))
    return {p for p in perms if p == p[::-1]}