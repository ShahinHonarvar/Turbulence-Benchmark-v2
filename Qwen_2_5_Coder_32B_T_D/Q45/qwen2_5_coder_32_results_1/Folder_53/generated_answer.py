from itertools import permutations

def palindromes_between_indices(s):
    s = ''.join([c.lower() for c in s[4:9] if c.isalpha()])
    p = {''.join(x) for x in permutations(s) if len(''.join(x)) >= 6}
    return {x for x in p if x == x[::-1]}