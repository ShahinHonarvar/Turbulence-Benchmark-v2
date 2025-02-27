from itertools import permutations

def palindromes_between_indices(s):
    substr = s[3:6].lower()
    all_perms = {''.join(p) for p in permutations(substr)}
    palindromes = {perm for perm in all_perms if len(perm) >= 4 and perm == perm[::-1]}
    return palindromes