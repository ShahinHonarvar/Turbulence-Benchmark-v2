from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:7])).lower()
    perms = {''.join(p) for p in permutations(letters, 6)}
    return {p for p in perms if p == p[::-1]}