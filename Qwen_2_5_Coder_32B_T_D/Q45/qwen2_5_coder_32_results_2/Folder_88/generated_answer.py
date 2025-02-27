from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[3:8].lower() if c.isalpha()]
    perms = set((''.join(p) for p in permutations(letters, 6)))
    return {p for p in perms if p == p[::-1]}