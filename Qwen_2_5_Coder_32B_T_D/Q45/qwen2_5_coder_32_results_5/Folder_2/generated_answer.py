from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[1:6] if c.isalpha()]
    letters = ''.join(letters).lower()
    perms = set([''.join(p) for p in permutations(letters, len(letters))])
    palindromes = {p for p in perms if len(p) >= 6 and p == p[::-1]}
    return palindromes