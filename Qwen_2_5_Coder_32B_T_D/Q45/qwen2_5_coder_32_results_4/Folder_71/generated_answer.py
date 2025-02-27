from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[1:4] if c.isalpha()]
    letters = [c.lower() for c in letters]
    perms = set(permutations(letters, len(letters)))
    palindromes = {tuple(p) for p in perms if p == tuple(reversed(p)) and len(p) >= 4}
    return {''.join(p) for p in palindromes}