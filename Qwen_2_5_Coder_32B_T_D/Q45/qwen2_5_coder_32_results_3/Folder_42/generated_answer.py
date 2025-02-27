from itertools import permutations

def palindromes_between_indices(s):
    s = s[6:10].lower()
    letters = [c for c in s if c.isalpha()]
    perms = set((''.join(p) for i in range(3, len(letters) + 1) for p in permutations(letters, i)))
    return {p for p in perms if p == p[::-1]}