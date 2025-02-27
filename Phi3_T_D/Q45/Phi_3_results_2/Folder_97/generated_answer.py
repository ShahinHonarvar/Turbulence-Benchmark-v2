from itertools import permutations
import string

def palindromes_between_indices(s):
    alphabet = set(string.ascii_letters)
    substring = ''.join((c for c in s[0:5] if c in alphabet)).lower()
    sub_permutations = {p for i in range(3, len(substring) + 1) for p in permutations(substring, i)}
    return {''.join(sub) for sub in sub_permutations if ''.join(sub[::-1]) == sub and len(sub) >= 3}