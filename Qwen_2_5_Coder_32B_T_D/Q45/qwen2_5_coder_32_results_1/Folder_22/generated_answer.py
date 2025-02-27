from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[5:7])).lower()
    perms = set((''.join(p) for p in permutations(letters, len(letters))))
    return {p for p in perms if len(p) >= 3 and p == p[::-1]}