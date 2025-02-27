from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:8].lower()
    letters = [c for c in s if c.isalpha()]
    p = set((''.join(p) for p in permutations(letters, len(letters))))
    return {x for x in p if x == x[::-1] and len(x) >= 7}