import itertools
    import string

def palindromes_between_indices(s):
    letters = ''.join(filter(lambda x: x in string.ascii_letters, s[:9])).lower()
    perms = set(itertools.permutations(letters, 7))
    palindromes = {''.join(p) for p in perms if p == p[::-1]}
    return palindromes