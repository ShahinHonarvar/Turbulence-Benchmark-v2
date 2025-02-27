from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:6]
    letters = [char for char in substring if char.isalpha()]
    all_permutations = set([''.join(p) for p in permutations(letters)])
    palindromes = set()
    for perm in all_permutations:
        if len(perm) >= 4 and perm.lower() == perm.lower()[::-1]:
            palindromes.add(perm)
    return palindromes