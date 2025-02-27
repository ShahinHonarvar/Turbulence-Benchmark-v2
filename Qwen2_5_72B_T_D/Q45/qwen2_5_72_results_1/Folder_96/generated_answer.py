from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:9].lower()
    char_permutations = set([''.join(p) for p in permutations(substring)])
    palindromes = set()
    for perm in char_permutations:
        if perm == perm[::-1] and len(perm) >= 6:
            palindromes.add(perm)
    return palindromes