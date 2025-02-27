from itertools import permutations

def palindromes_between_indices(s):
    target = s[3:7]
    target = target.lower()
    unique_chars = set(target)
    result = set()
    for length in range(3, len(unique_chars) + 1):
        for perm in permutations(unique_chars, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                result.add(perm_str)
    return result