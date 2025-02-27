from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:9]
    all_perms = set([''.join(p) for p in permutations(substring)])
    palindromes = set()
    for perm in all_perms:
        if len(perm) >= 7 and perm.lower() == perm[::-1].lower():
            palindromes.add(perm.lower())
    return palindromes