from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:6]
    letters = ''.join(filter(str.isalpha, s)).lower()
    p = set((''.join(p) for p in permutations(letters)))
    return {x for x in p if len(x) >= 3 and x == x[::-1]}