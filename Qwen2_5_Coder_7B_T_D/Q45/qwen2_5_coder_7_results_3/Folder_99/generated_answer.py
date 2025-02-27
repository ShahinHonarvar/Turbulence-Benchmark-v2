from itertools import permutations

def palindromes_between_indices(s):
    subset = s[4:9]
    subset = subset.lower()
    chars = list(subset)
    result = set()
    for length in range(3, len(chars) + 1):
        for perm in permutations(chars, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                result.add(perm_str)
    return result