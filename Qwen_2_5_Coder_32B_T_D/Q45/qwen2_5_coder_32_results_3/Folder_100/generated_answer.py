import itertools
    import string

def palindromes_between_indices(s):
    letters = ''.join([c.lower() for c in s[:6] if c in string.ascii_letters])
    perms = set((''.join(p) for p in itertools.permutations(letters, 6)))
    return {p for p in perms if p == p[::-1]}