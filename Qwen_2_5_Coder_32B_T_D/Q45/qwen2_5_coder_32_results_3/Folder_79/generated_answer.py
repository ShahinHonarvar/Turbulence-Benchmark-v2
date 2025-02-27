from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:8] if c.isalpha()]
    pals = set()
    for perm in permutations(letters, len(letters)):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 3:
            pals.add(p)
    return pals