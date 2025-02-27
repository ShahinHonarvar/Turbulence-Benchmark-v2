from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(sorted([c.lower() for c in s[1:6] if c.isalpha()]))
    perms = set(permutations(letters, 6))
    palindromes = {p for p in perms if p == p[::-1]}
    return set([''.join(p) for p in palindromes])