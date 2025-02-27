from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:5].lower()
    letters = [c for c in s if c.isalpha()]
    perms = set((''.join(p) for p in permutations(letters, len(letters))))
    return {p for p in perms if len(p) >= 3 and p == p[::-1]}