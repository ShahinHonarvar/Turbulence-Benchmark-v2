from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 3:
        return set()
    subset_s = s[1:3].lower()
    unique_perms = set()
    for perm in permutations(subset_s):
        candidate = ''.join(perm)
        if len(candidate) >= 3 and candidate == candidate[::-1]:
            unique_perms.add(candidate)
    return unique_perms