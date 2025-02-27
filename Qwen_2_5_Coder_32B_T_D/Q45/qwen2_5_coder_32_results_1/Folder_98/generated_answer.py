from itertools import permutations
    from collections import Counter
    import string

def palindromes_between_indices(s):
    s = s[3:6].lower()
    letters = [c for c in s if c in string.ascii_lowercase]
    perms = set((''.join(p) for p in permutations(letters, len(letters))))
    palindromes = {p for p in perms if p == p[::-1] and len(p) >= 4}
    return palindromes