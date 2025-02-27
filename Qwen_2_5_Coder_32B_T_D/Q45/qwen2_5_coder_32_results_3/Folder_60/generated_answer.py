from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:7].lower()
    letters = [c for c in s if c.isalpha()]
    p = set([''.join(i) for i in permutations(letters, 4)])
    return {x for x in p if x == x[::-1]}