from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:7].lower()
    result = set()
    for perm in permutations(s):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 4:
            result.add(perm_str)
    return result