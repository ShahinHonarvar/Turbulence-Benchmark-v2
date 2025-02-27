from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c.lower() for c in s[7:9] if c.isalpha()])
    perms = set((''.join(p) for p in permutations(letters, len(letters))))
    return {p for p in perms if len(p) >= 3 and p == p[::-1]}