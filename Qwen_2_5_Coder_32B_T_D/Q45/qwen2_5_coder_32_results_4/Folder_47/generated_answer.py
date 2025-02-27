from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:8] if c.isalpha()]
    perms = set(permutations(letters, len(letters)))
    palindromes = {''.join(p) for p in perms if len(p) >= 5 and p == p[::-1]}
    return palindromes