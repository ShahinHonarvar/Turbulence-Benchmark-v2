from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:7]
    all_perms = {''.join(p) for p in permutations(substring)}
    all_perms_lower = {perm.lower() for perm in all_perms}
    palindromes = {perm for perm in all_perms_lower if perm == perm[::-1] and len(perm) >= 3}
    return palindromes