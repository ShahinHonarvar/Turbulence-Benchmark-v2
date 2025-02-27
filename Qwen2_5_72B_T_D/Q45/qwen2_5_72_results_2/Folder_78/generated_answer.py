from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:9]
    chars = [char.lower() for char in substring if char.isalpha()]
    all_perms = set([''.join(p) for p in permutations(chars, len(chars))])
    valid_palindromes = {perm for perm in all_perms if perm == perm[::-1] and len(perm) >= 3}
    return valid_palindromes