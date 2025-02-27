from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:5].lower()
    original_len = len(substring)
    charset = set(substring)
    results = set()
    for length in range(original_len, 0, -1):
        for perm in permutations(charset, length):
            perm_str = ''.join(perm)
            for i in range(1, len(perm_str) // 2 + 1):
                if perm_str[:i] == perm_str[-i:]:
                    results.add(perm_str)
                    break
    return results