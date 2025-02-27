from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:8] if c.isalpha()]
    p = set((''.join(p) for p in permutations(letters)))
    return {x for x in p if len(x) >= 5 and x == x[::-1]}