from itertools import permutations
    import string

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:7] if c.lower() in string.ascii_lowercase]
    perms = set(permutations(letters, len(letters)))
    palindromes = {''.join(p) for p in perms if len(p) >= 3 and p == p[::-1]}
    return palindromes