from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[6:9] if c.isalpha()]
    perms = set((''.join(p) for p in permutations(letters, len(letters))))
    palindromes = {w for w in perms if len(w) >= 4 and w == w[::-1]}
    return palindromes