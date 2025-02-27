from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:7].lower()
    letter_set = set(substring)
    result_set = set()
    for r in range(3, len(substring) + 1):
        for perm in permutations(substring, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                result_set.add(perm_str)
    return result_set