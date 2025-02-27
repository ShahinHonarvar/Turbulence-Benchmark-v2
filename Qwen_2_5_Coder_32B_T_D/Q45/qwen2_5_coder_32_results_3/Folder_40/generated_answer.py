from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:10] if c.isalpha()]
    perms = set(permutations(letters, min(9, len(letters))))
    palindromes = {''.join(p) for p in perms if len(p) >= 7 and p == p[::-1]}
    return palindromes