from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:9].lower()
    all_perms = {''.join(p) for p in permutations(substring)}
    result = {perm + perm[::-1] for perm in all_perms if len(perm + perm[::-1]) >= 4}
    return result