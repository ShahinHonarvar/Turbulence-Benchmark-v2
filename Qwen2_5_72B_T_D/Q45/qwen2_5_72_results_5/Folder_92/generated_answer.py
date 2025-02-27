from itertools import permutations

def palindromes_between_indices(s):
    substr = s[4:8].lower()
    perms = set([''.join(p) for p in permutations(substr)])
    palindromes = {perm for perm in perms if len(perm) >= 4 and perm == perm[::-1]}
    return palindromes