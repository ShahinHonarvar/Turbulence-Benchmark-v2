from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:5].lower()
    unique_chars = ''.join(set(substring))
    all_perms = set([''.join(p) for p in permutations(unique_chars, len(unique_chars))])
    palindromes = {perm for perm in all_perms if perm == perm[::-1] and len(perm) >= 5}
    return palindromes