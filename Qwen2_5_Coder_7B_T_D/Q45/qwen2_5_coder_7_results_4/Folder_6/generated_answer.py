from itertools import permutations

def palindromes_between_indices(s):
    s = s[:8].lower()
    chars = set(s)
    result = set()
    for length in range(4, len(s) + 1):
        for perm in permutations(chars, length):
            if perm == perm[::-1]:
                result.add(''.join(perm))
    return result