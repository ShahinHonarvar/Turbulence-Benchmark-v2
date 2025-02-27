from itertools import permutations

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[4:9] if c.isalpha()]
    perms = set((''.join(p) for p in permutations(chars, len(chars))))
    palindromes = {p for p in perms if len(p) >= 4 and p == p[::-1]}
    return palindromes