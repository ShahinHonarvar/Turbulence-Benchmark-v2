from itertools import permutations

def palindromes_between_indices(s):
    substring = s[5:8].lower()
    unique_chars = set(substring)
    perms = set([''.join(p) for p in permutations(substring)])
    palindromes = {perm for perm in perms if len(perm) >= 3 and perm == perm[::-1]}
    return palindromes