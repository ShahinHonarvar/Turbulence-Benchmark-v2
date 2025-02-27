from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:8].lower()
    letters = [c for c in s if c.isalpha()]
    perms = set((''.join(p) for p in permutations(letters, len(letters))))
    return {p for p in perms if len(p) >= 4 and p == p[::-1]}