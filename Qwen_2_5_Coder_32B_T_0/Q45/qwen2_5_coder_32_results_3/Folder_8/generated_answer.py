from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:6])).lower()
    perms = set((''.join(p) for p in permutations(letters, 5)))
    return {p for p in perms if p == p[::-1]}