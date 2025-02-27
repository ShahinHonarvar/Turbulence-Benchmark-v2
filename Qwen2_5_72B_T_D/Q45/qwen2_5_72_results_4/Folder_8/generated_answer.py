from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:6].lower()
    letters = ''.join(sorted(set(substring), key=substring.index))
    all_permutations = set([''.join(p) for p in permutations(letters)])
    palindromes = {perm for perm in all_permutations if perm == perm[::-1] and len(perm) >= 5}
    return palindromes