from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:7].lower()
    all_perms = set([''.join(p) for p in permutations(substring)])
    palindromes = set([p for p in all_perms if p == p[::-1] and len(p) >= 3])
    return palindromes