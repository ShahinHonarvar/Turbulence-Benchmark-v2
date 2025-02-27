from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:9] if c.isalpha()]
    perms = set(permutations(letters, 6))
    palindromes = {''.join(p) for p in perms if p == p[::-1]}
    return palindromes