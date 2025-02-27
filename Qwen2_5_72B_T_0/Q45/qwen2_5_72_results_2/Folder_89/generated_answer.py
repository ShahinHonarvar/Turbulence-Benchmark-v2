from itertools import permutations

def palindromes_between_indices(s):
    substring = s[5:10].lower()
    unique_chars = ''.join(set(substring))
    perms = set([''.join(p) for p in permutations(unique_chars)])
    palindromes = {perm for perm in perms if len(perm) >= 6 and perm == perm[::-1]}
    return palindromes