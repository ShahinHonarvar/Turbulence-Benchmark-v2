from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:8] if c.isalpha()]
    perms = set((''.join(p) for p in permutations(letters, 6)))
    palindromes = {p for p in perms if p == p[::-1]}
    return palindromes