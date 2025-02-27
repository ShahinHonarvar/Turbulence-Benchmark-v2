from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c for c in s[:4] if c.isalpha()]).lower()
    perms = set([''.join(p) for p in permutations(letters, len(letters))])
    return {p for p in perms if len(p) >= 4 and p == p[::-1]}