from collections import Counter
    from itertools import permutations
    import string

def palindromes_between_indices(s):
    letters = ''.join([c for c in s[2:8].lower() if c in string.ascii_lowercase])
    perms = set(permutations(letters, 6))
    palindromes = {''.join(p) for p in perms if p == p[::-1]}
    return palindromes