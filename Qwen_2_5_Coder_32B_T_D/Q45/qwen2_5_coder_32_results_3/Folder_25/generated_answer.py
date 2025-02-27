from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c.lower() for c in s[1:5] if c.isalpha()])
    pals = set()
    for perm in permutations(letters):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 3:
            pals.add(p)
    return pals