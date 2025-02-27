from itertools import permutations

def palindromes_between_indices(s):
    middle = s[4:9]
    unique_chars = sorted(set(middle.lower()))
    if len(unique_chars) < 6:
        return set()
    results = set()
    for length in range(6, len(unique_chars) + 1):
        for perm in permutations(unique_chars, length):
            candidate = ''.join(perm[:4]) + (perm[4] if length > 5 else '') + ''.join(reversed(perm[:4]))
            results.add(candidate)
    return results