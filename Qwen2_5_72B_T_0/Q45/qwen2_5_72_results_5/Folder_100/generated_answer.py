from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:6].lower()
    unique_chars = ''.join(set(substring))
    all_perms = set([''.join(p) for p in permutations(unique_chars)])
    palindromes = {perm for perm in all_perms if len(perm) >= 6 and perm == perm[::-1]}
    return palindromes