from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:8].lower()
    letters = [c for c in s if c.isalpha()]
    p = set()
    for i in range(3, len(letters) + 1):
        for perm in permutations(letters, i):
            w = ''.join(perm)
            if w == w[::-1]:
                p.add(w)
    return p