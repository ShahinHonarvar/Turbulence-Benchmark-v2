from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c.lower() for c in s[:6] if c.isalpha()])
    pals = set()
    for perm in permutations(letters, min(5, len(letters))):
        p = ''.join(perm)
        if len(p) >= 4 and p == p[::-1]:
            pals.add(p)
    return pals