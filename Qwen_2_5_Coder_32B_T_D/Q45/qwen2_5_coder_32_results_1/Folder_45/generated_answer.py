from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:10] if c.isalpha()]
    perms = set(permutations(letters, len(letters)))
    palindromes = set()
    for p in perms:
        perm_str = ''.join(p)
        if perm_str == perm_str[::-1] and len(perm_str) >= 4:
            palindromes.add(perm_str)
    return palindromes