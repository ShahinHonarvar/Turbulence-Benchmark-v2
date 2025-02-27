from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:8].lower()
    char_list = list(substring)
    all_perms = {''.join(p) for p in permutations(char_list, 7)}
    palindromes = {perm for perm in all_perms if perm == perm[::-1]}
    return palindromes