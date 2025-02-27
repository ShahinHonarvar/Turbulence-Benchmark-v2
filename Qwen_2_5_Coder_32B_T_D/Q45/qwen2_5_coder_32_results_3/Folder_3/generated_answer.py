from itertools import permutations

def palindromes_between_indices(s):
    s = s[7:10].lower()
    letters = [c for c in s if c.isalpha()]
    p = set((''.join(x) for x in permutations(letters, len(letters))))
    return {x for x in p if len(x) >= 3 and x == x[::-1]}