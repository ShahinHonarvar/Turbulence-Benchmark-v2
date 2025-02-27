from itertools import permutations

def palindromes_between_indices(s):
    substring = s[5:8]
    letters = [char.lower() for char in substring if char.isalpha()]
    all_perms = {''.join(p) for p in permutations(letters)}
    palindromes = {perm for perm in all_perms if len(perm) >= 4 and perm == perm[::-1]}
    return palindromes