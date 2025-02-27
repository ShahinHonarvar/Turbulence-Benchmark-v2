from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:7])).lower()
    perms = set(permutations(letters, 6))
    return {''.join(p) for p in perms if p == p[::-1]}