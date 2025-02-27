from itertools import permutations

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:9])).lower()
    perms = set((''.join(p) for p in permutations(s, 7)))
    return {p for p in perms if p == p[::-1]}