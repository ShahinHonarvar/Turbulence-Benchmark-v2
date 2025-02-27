from itertools import permutations

def palindromes_between_indices(s):
    s = s[:3].lower()
    letters = [c for c in s if c.isalpha()]
    perms = set((''.join(p) for p in permutations(letters, min(3, len(letters)))))
    return {p for p in perms if p == p[::-1] and len(p) >= 3}