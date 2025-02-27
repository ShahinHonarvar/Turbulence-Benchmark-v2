from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[4:10].lower() if c.isalpha()]
    perms = set(permutations(letters, len(letters)))
    palindromes = {''.join(p) for p in perms if len(p) >= 6 and p == p[::-1]}
    return palindromes