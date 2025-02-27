from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:6] if c.isalpha()]
    p = set((''.join(x) for x in permutations(letters, len(letters))))
    return {x for x in p if len(x) >= 4 and x == x[::-1]}