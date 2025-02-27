from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:6])).lower()
    perms = set(permutations(letters, len(letters)))
    palindromes = set()
    for perm in perms:
        p = ''.join(perm)
        if len(p) >= 4 and p == p[::-1]:
            palindromes.add(p)
    return palindromes