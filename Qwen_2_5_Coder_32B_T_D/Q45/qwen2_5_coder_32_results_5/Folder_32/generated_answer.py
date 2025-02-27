from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c for c in s[1:8] if c.isalpha()]).lower()
    p = set()
    for perm in permutations(letters, len(letters)):
        perm_str = ''.join(perm)
        if len(perm_str) >= 5 and perm_str == perm_str[::-1]:
            p.add(perm_str)
    return p