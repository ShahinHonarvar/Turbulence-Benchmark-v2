from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:8].lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for r in range(3, len(s) + 1):
        for perm in permutations(s, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1] and all((c in letters for c in perm_str)):
                palindromes.add(perm_str)
    return palindromes