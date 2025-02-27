from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:9].lower()
    result = set()
    for r in range(4, len(s) + 1):
        for p in permutations(s, r):
            if p == p[::-1]:
                result.add(''.join(p))
    return result