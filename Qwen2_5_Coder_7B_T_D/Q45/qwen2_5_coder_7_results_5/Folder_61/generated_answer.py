from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    target_len = 7
    result = set()
    for perm in permutations(s[:8], target_len):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            result.add(candidate)
    return result