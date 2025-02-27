from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(sorted(filter(str.isalpha, s[5:7].lower())))
    p = set()
    for r in range(3, len(letters) + 1):
        for perm in permutations(letters, r):
            s = ''.join(perm)
            if s == s[::-1]:
                p.add(s)
    return p