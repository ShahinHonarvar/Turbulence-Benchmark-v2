from itertools import permutations

def palindromes_between_indices(s):
    l = s[6:10].lower()
    letters = [c for c in l if c.isalpha()]
    p = set([''.join(x) for x in permutations(letters)])
    return {x for x in p if len(x) >= 4 and x == x[::-1]}