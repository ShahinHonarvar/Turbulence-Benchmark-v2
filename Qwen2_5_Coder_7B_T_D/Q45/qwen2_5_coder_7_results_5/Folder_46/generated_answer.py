from itertools import permutations

def palindromes_between_indices(s):
    subset = s[4:10]
    unique_chars = set(subset.lower())
    palindromes = set()
    for r in range(6, len(unique_chars) + 1):
        for perm in permutations(unique_chars, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes