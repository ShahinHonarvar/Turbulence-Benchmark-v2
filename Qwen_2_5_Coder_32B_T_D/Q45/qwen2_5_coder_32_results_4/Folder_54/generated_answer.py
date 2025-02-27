from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:10])).lower()
    perms = set(permutations(letters, min(9, len(letters))))
    palindromes = {p for p in perms if p == p[::-1] and len(p) >= 4}
    return palindromes