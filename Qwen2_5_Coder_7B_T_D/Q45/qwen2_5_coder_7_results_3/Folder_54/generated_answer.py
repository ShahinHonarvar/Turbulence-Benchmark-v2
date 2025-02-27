from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10]
    s = s.lower()
    chars = list(s)
    result = set()
    for length in range(4, len(chars) + 1):
        for perm in permutations(chars, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                result.add(perm_str)
    return result