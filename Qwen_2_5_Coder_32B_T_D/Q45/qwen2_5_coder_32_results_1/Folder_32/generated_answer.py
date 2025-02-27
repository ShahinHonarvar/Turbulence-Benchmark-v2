from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:8])).lower()
    perms = set((''.join(p) for p in permutations(letters, len(letters))))
    return {p for p in perms if len(p) >= 5 and p == p[::-1]}