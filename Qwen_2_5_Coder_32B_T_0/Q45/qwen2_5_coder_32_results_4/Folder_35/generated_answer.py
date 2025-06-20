from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:5])).lower()
    perms = set((''.join(p) for p in permutations(letters, len(letters))))
    palindromes = {p for p in perms if len(p) >= 4 and p == p[::-1]}
    return palindromes