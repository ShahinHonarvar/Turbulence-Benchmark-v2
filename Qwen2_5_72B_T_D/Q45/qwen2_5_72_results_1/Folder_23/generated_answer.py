from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:7].lower()
    all_perms = set([''.join(p) for p in permutations(substring)])
    result = set()
    for perm in all_perms:
        if len(perm) >= 4 and perm == perm[::-1]:
            result.add(perm)
    return result