from itertools import permutations

def palindromes_between_indices(s):
    s = s[:8].lower()
    letters = set(s)
    result = set()
    for r in range(6, len(letters) + 1):
        for perm in permutations(letters, r):
            p = ''.join(perm)
            if p == p[::-1]:
                result.add(p)
    return result