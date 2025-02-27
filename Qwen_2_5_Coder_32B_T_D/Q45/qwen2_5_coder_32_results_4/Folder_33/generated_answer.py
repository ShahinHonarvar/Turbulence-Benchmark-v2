from itertools import permutations

def palindromes_between_indices(s):
    letters = sorted([c.lower() for c in s[7:10] if c.isalpha()])
    pals = set()
    for perm in permutations(letters):
        p = ''.join(perm)
        if len(p) >= 4 and p == p[::-1]:
            pals.add(p)
    return pals