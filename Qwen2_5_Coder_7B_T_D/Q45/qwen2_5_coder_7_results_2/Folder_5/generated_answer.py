from itertools import permutations

def palindromes_between_indices(s):
    subset = s[4:9]
    subset = ''.join(filter(str.isalpha, subset)).lower()
    unique_chars = set(subset)
    if len(unique_chars) < 2:
        return set()
    perms = set((''.join(p) for p in permutations(unique_chars, 4)))
    palindromes = {p for p in perms if p == p[::-1]}
    return palindromes