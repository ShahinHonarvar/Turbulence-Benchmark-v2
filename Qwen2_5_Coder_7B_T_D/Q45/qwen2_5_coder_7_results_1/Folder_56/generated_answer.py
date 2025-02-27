from itertools import permutations

def palindromes_between_indices(s):
    result = set()
    for perm in permutations(s[5:10], 5):
        candidate = ''.join(perm).lower()
        if candidate == candidate[::-1]:
            result.add(candidate)
    return result