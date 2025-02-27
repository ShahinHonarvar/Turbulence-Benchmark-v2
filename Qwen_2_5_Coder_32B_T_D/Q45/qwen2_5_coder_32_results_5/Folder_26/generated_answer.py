from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:7].lower()
    letters = [c for c in s if c.isalpha()]
    perms = set(permutations(letters, len(letters)))
    palindromes = {''.join(p) for p in perms if len(p) >= 3 and p == p[::-1]}
    return palindromes