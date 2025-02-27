from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:5])).lower()
    if len(letters) < 4:
        return set()
    perms = set((''.join(p) for p in permutations(letters)))
    return {p for p in perms if p == p[::-1] and len(p) >= 4}