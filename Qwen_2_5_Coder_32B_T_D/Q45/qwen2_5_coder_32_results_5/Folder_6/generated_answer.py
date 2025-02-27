from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:8])).lower()
    perms = set(permutations(letters, 4))
    palindromes = {p for p in perms if p == p[::-1]}
    return {''.join(p) for p in palindromes}