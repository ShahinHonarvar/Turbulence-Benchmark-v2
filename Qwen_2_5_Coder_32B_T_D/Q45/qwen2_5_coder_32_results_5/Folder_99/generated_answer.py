from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:9])).lower()
    p = set()
    for r in range(3, len(letters) + 1):
        for perm in permutations(letters, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                p.add(perm_str)
    return p