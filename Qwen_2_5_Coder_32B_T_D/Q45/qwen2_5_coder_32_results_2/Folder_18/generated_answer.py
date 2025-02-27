from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:7] if c.isalpha()]
    if len(letters) < 3:
        return set()
    perms = set(permutations(letters, len(letters)))
    palindromes = {''.join(p) for p in perms if p == p[::-1] and len(p) >= 3}
    return palindromes