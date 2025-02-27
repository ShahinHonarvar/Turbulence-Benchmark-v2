from itertools import permutations

def palindromes_between_indices(s):
    sub = s[5:10]
    unique_letters = set(sub.lower())
    sub_permutations = (''.join(p) for p in permutations(unique_letters) if len(p) >= 5)
    return set((''.join(x) + x[::-1] for x in sub_permutations if ''.join(x) == ''.join(x)[::-1]))