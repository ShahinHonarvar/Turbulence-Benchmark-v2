import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[0:6])).lower()
    perms = set((''.join(p) for p in itertools.permutations(letters, 4)))
    return {p for p in perms if p == p[::-1]}