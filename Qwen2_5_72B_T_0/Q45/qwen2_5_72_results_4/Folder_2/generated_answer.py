from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:6].lower()
    unique_chars = ''.join(set(substring))
    all_perms = set([''.join(p) for p in permutations(unique_chars * 6, 6)])
    palindromes = {perm for perm in all_perms if perm == perm[::-1]}
    return palindromes