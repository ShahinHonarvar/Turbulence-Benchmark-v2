from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:5].lower()
    seen_chars = set(substring)
    result = set()
    for length in range(3, 5):
        for perm in permutations(seen_chars, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                result.add(perm_str)
    return result