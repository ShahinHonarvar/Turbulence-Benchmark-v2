from itertools import permutations
    import re

def palindromes_between_indices(s):
    s = s.lower()
    letters = set(s[1:8])
    palindromes = set()
    for perm in permutations(letters, 7):
        perm_str = ''.join(perm)
        if re.fullmatch('^[a-z]*$', perm_str) and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes