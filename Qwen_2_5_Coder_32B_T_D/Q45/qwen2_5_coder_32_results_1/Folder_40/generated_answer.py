from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:10])).lower()
    p = set()
    for perm in permutations(letters, len(letters)):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 7:
            p.add(perm_str)
    return p