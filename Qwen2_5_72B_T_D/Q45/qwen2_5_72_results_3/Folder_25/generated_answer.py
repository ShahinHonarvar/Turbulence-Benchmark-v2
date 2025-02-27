from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:5].lower()
    unique_chars = ''.join(set(substring))
    all_perms = set([''.join(p) for i in range(3, len(unique_chars) + 1) for p in permutations(unique_chars, i)])
    palindromes = {perm for perm in all_perms if perm == perm[::-1] and len(perm) >= 3}
    return palindromes