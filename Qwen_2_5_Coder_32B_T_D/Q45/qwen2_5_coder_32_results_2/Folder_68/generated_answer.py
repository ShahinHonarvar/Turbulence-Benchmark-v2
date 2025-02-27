from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:9].lower()
    letters = [c for c in s if c.isalpha()]
    result = set()
    for r in range(4, len(letters) + 1):
        for p in permutations(letters, r):
            p_str = ''.join(p)
            if p_str == p_str[::-1]:
                result.add(p_str)
    return result