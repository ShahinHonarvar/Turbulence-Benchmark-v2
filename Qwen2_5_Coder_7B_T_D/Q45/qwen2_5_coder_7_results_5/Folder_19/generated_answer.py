from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:8].lower()
    chars = set(s)
    result = set()
    for length in range(7, len(chars) + 1):
        for perm in permutations(chars, length):
            half = ''.join(perm)
            full = half + half[-2::-1]
            if full in s:
                result.add(full)
    return result