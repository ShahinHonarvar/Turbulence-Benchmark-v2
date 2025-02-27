from itertools import permutations

def palindromes_between_indices(s):
    letters = {c.lower() for c in s[3:7] if c.isalpha()}
    perms = [''.join(p) for i in range(3, 7) for p in permutations(letters, i)]
    return {p for p in perms if p == p[::-1]}