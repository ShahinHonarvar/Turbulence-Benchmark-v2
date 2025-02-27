from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:8] if c.isalpha()]
    n = len(letters)
    result = set()
    for perm in permutations(letters):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 7:
            result.add(p)
    return result