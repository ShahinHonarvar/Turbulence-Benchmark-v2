from itertools import permutations

def palindromes_between_indices(s):
    substr = s[3:9]
    result = set()
    for length in range(6, len(substr) + 1):
        for p in permutations(substr.lower(), length):
            s = ''.join(p)
            if s == s[::-1]:
                result.add(s)
    return result