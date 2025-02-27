from itertools import permutations

def palindromes_between_indices(s):
    start, end = (3, 9)
    substr = s[start - 1:end].lower()
    letters = ''.join(filter(str.isalpha, substr))
    if len(letters) < 7:
        return set()
    perms = set(permutations(letters, 7))
    return {''.join(p) for p in perms if p == p[::-1]}