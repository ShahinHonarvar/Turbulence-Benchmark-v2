from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[4:9] if c.isalpha()]
    letters = set((c.lower() for c in letters))
    perms = set((''.join(p) for p in permutations(letters, 5)))
    return {p for p in perms if p == p[::-1]}