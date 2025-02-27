from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:5])).lower()
    perms = set((''.join(p) for p in permutations(letters, 3)))
    palindromes = {p for p in perms if p == p[::-1]}
    return palindromes