from itertools import permutations

def palindromes_between_indices(s):
    substr = s[3:8].lower()
    unique_chars = set(substr)
    palindromes = set()
    for r in range(6, len(substr) + 1):
        for perm in permutations(unique_chars, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes