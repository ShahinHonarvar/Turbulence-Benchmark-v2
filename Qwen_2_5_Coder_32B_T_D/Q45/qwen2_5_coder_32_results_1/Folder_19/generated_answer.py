from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:8])).lower()
    p = set()
    for perm in permutations(letters, 7):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1]:
            p.add(perm_str)
    return p