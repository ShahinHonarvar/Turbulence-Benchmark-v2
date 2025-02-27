from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:8])).lower()
    p = set((''.join(p) for p in permutations(letters, 5)))
    return {x for x in p if x == x[::-1]}