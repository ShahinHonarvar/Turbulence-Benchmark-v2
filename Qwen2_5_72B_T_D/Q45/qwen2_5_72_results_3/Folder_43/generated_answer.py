from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:6].lower()
    unique_chars = set(substring)
    all_permutations = [''.join(p) for p in permutations(substring)]
    palindromes = {perm for perm in all_permutations if len(perm) >= 4 and perm == perm[::-1]}
    return palindromes