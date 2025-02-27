from itertools import permutations
from collections import Counter

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = set(s)
    result = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result