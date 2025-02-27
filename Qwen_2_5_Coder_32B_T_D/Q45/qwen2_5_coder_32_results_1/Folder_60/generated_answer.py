from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:7] if c.isalpha()]
    perms = set([''.join(p) for p in permutations(letters)])
    palindromes = {p for p in perms if len(p) >= 4 and p == p[::-1]}
    return palindromes