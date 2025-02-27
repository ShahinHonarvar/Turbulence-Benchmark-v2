from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[6:10].lower() if c.isalpha()]
    perms = set([''.join(p) for p in permutations(letters)])
    palindromes = {p for p in perms if len(p) >= 5 and p == p[::-1]}
    return palindromes