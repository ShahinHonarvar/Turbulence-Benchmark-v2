from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(s):
    letters = ''.join([c.lower() for c in s[3:7] if c.lower() in ascii_lowercase])
    perms = set([''.join(p) for p in permutations(letters, 3)])
    return {p for p in perms if p == p[::-1]}