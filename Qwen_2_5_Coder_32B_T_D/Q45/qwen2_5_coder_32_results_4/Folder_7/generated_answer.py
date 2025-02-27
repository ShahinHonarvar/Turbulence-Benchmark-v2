from itertools import permutations

def palindromes_between_indices(s):
    letters = sorted([c.lower() for c in s[1:10] if c.isalpha()])
    p = set()
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        if len(perm_str) >= 7 and perm_str == perm_str[::-1]:
            p.add(perm_str)
    return p