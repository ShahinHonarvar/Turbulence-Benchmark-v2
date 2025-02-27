from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c.lower() for c in s[5:8] if c.isalpha()])
    p = set([''.join(p) for p in permutations(letters, len(letters))])
    return {x for x in p if len(x) >= 3 and x == x[::-1]}