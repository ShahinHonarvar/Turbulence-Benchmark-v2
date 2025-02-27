from itertools import permutations

def palindromes_between_indices(s):
    substr = s[2:9]
    possible_perms = set()
    for length in range(4, len(substr) + 1):
        possible_perms.update([''.join(p) for p in permutations(substr, length)])
    return {perm.lower() for perm in possible_perms if perm.lower() == perm.lower()[::-1]}