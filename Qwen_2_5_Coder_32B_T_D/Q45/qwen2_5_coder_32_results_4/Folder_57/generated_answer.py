from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:6] if c.isalpha()]
    perms = set(permutations(letters))
    palindromes = {''.join(p) for p in perms if len(p) >= 5 and p == p[::-1]}
    return palindromes