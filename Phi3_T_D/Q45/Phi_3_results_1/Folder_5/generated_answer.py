from itertools import permutations

def palindromes_between_indices(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sub_string = s[4:9]
    perms = set((''.join(p) for p in permutations(sub_string)))
    palindromes = set()
    for perm in perms:
        if 2 < len(perm) < 9:
            perm_lower = perm.lower()
            if perm_lower == perm_lower[::-1]:
                palindromes.add(perm)
    return palindromes