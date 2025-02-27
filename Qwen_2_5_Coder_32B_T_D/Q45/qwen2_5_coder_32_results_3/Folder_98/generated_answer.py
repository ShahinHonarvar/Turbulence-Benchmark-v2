from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c.lower() for c in s[3:6] if c.isalpha()])
    perms = set(permutations(letters, len(letters)))
    palindromes = {''.join(p) for p in perms if len(p) >= 4 and p == p[::-1]}
    return palindromes