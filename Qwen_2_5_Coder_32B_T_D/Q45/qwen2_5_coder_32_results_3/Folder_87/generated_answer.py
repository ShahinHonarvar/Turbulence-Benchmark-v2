from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:10] if c.isalpha()]
    p = set()
    for l in range(3, len(letters) + 1):
        for perm in permutations(letters, l):
            s = ''.join(perm)
            if s == s[::-1]:
                p.add(s)
    return p