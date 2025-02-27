from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[7:9] if c.isalpha()]
    perms = set((''.join(p).lower() for r in range(3, len(letters) + 1) for p in permutations(letters, r)))
    return {p for p in perms if p == p[::-1]}