from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[:3] if c.isalpha()]
    letters = set(letters)
    perms = set([''.join(p).lower() for p in permutations(letters, 3)])
    return {p for p in perms if p == p[::-1]}