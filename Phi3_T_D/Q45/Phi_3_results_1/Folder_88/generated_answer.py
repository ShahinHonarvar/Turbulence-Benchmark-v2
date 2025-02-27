import itertools

def palindromes_between_indices(s):
    substring = s[3:8].lower()
    chars = set(substring)
    results = set()
    for length in range(6, len(substring) + 1):
        for perm in itertools.permutations(chars, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                results.add(perm_str)
    return results