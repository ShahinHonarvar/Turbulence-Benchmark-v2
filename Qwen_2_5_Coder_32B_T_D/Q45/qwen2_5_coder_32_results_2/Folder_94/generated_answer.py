from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:5] if c.isalpha()]
    perms = set((''.join(p) for p in permutations(letters, len(letters))))
    palindromes = {p for p in perms if len(p) >= 3 and p == p[::-1]}
    return palindromes