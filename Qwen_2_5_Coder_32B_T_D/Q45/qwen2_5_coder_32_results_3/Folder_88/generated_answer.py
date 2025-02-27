import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:8])).lower()
    perms = set(itertools.permutations(letters))
    palindromes = {p for p in perms if len(p) >= 6 and p == p[::-1]}
    return palindromes