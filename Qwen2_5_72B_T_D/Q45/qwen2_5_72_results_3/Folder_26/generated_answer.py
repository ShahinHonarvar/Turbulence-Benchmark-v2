from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:7].lower()
    perms = {''.join(p) for p in permutations(substring)}
    palindromes = {perm for perm in perms if len(perm) >= 3 and perm == perm[::-1]}
    return palindromes