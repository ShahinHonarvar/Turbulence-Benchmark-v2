from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[6:9])).lower()
    p = {x for x in permutations(letters, min(4, len(letters)))}
    return {s for s in (''.join(x) for x in p) if s == s[::-1] and len(s) >= 4}