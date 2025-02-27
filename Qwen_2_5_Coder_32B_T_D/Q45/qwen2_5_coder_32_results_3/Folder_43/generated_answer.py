from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:6])).lower()
    perms = set((''.join(p) for p in permutations(letters, min(4, len(letters)))))
    return {p for p in perms if p == p[::-1]}