from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:7])).lower()
    result = set()
    for r in range(3, len(letters) + 1):
        for p in permutations(letters, r):
            perm = ''.join(p)
            if perm == perm[::-1]:
                result.add(perm)
    return result