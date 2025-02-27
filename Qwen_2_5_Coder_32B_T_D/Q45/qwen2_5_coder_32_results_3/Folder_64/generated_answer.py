import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:10] if c.isalpha()]
    perms = set(itertools.permutations(letters, 5))
    palindromes = {p for p in perms if p == p[::-1]}
    return palindromes