from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:5].lower()
    all_perms = {''.join(p) for p in permutations(substring)}
    palindromes = {perm for perm in all_perms if len(perm) >= 4 and perm == perm[::-1]}
    return palindromes