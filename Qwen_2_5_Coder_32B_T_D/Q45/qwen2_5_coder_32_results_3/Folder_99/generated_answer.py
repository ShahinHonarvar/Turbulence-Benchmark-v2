from itertools import permutations

def palindromes_between_indices(s):
    letters = sorted([c.lower() for c in s[4:9] if c.isalpha()])
    perms = set((''.join(p) for p in permutations(letters, len(letters))))
    palindromes = {perm for perm in perms if perm == perm[::-1] and len(perm) >= 3}
    return palindromes