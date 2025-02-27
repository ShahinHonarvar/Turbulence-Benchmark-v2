from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(sorted([c.lower() for c in s[1:6] if c.isalpha()]))
    p = {''.join(p) for p in permutations(letters, len(letters))}
    return {x for x in p if x == x[::-1] and len(x) >= 4}