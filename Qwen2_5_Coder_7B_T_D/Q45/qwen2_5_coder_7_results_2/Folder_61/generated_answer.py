from itertools import permutations

def palindromes_between_indices(s):
    s = s[:8].lower()
    letters = sorted(set(s))
    palindromes = set()
    for r in range(7, len(s) + 1):
        for perm in permutations(letters, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes