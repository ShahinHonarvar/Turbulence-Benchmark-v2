from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:6] if c.isalpha()]
    letters = [c.lower() for c in letters]
    perms = set(permutations(letters, len(letters)))
    palindromes = set()
    for p in perms:
        k = ''.join(p)
        if len(k) >= 3 and k == k[::-1]:
            palindromes.add(k)
    return palindromes