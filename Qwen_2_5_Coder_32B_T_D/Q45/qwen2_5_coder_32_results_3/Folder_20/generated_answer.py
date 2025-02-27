from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:9] if c.isalpha()]
    letters = ''.join(letters).lower()
    perms = set(permutations(letters, 4))
    palindromes = {''.join(p) for p in perms if ''.join(p) == ''.join(p)[::-1]}
    return palindromes