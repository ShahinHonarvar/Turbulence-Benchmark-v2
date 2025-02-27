import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:5])).lower()
    perms = set(itertools.permutations(letters, 5))
    palindromes = {''.join(p) for p in perms if p == p[::-1]}
    return palindromes