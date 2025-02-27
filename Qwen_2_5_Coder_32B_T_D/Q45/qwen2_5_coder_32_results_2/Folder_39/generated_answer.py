import itertools
    from collections import Counter

def palindromes_between_indices(s):
    letters = ''.join(sorted([c for c in s[2:6] if c.isalpha()])).lower()
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in set(itertools.permutations(letters, r)):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes