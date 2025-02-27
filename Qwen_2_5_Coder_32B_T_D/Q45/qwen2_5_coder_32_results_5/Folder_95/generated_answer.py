from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[7:9])).lower()
    p = set((''.join(p) for p in permutations(letters)))
    return {x for x in p if len(x) >= 3 and x == x[::-1]}