from itertools import permutations
    from collections import Counter
    import string

def palindromes_between_indices(s):
    s = s[4:10].lower()
    letters = [c for c in s if c in string.ascii_lowercase]
    perms = set((''.join(p) for p in permutations(letters)))
    palindromes = {p for p in perms if len(p) >= 3 and p == p[::-1]}
    return palindromes