from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:8].lower()
    letters = ''.join(filter(str.isalpha, s))
    p = set()
    for r in range(3, len(letters) + 1):
        for perm in permutations(letters, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                p.add(perm_str)
    return p