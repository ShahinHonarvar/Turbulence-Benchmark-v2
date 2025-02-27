from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[6:9] if c.isalpha()]
    perms = set((''.join(p) for p in permutations(letters, min(8, len(letters)))))
    return {p for p in perms if len(p) >= 4 and p == p[::-1]}