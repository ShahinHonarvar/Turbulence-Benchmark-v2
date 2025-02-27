from itertools import permutations

def palindromes_between_indices(s):
    result = set()
    letters = s[1:6]
    for perm in permutations(letters):
        perm_str = ''.join(perm).lower()
        if len(perm_str) >= 5 and perm_str == perm_str[::-1]:
            result.add(perm_str)
    return result