from itertools import permutations

def palindromes_between_indices(s):
    subset = s[2:7]
    subset = ''.join(filter(str.isalpha, subset)).lower()
    unique_chars = ''.join(sorted(set(subset)))
    result = set()
    for r in range(4, len(unique_chars) + 1):
        for p in permutations(unique_chars, r):
            half = ''.join(p)
            full = half + half[::-1]
            if full in result or half != half[::-1]:
                continue
            result.add(full)
    return result