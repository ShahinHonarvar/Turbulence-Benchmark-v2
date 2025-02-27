from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c for c in s[2:6] if c.isalpha()]).lower()
    perms = set((''.join(p) for p in permutations(letters)))
    palindromes = {p for p in perms if len(p) >= 4 and p == p[::-1]}
    return palindromes