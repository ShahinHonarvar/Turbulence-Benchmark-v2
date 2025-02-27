from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(s):
    letters = ''.join([c for c in s[:4].lower() if c in ascii_lowercase])
    p = set((''.join(p) for p in permutations(letters, 4)))
    return {x for x in p if x == x[::-1]}