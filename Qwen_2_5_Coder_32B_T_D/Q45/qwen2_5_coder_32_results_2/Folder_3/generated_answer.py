from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[7:10] if c.isalpha()]
    pals = set()
    for perm in permutations(letters):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 3:
            pals.add(p)
    return pals