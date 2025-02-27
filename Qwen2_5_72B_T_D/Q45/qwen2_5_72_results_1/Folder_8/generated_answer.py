from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:6].lower()
    unique_chars = ''.join(set(substring))
    all_perms = set([''.join(p) for i in range(5, len(unique_chars) + 1) for p in permutations(unique_chars, i)])
    palindromes = {perm for perm in all_perms if len(perm) >= 5 and perm == perm[::-1]}
    return palindromes