from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:6] if c.isalpha()]
    perms = set(permutations(letters, 4))
    palindromes = {p for p in perms if p == p[::-1]}
    return {''.join(p) for p in palindromes}