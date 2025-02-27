from itertools import permutations

def palindromes_between_indices(s):
    letters = sorted([c.lower() for c in s[4:8] if c.isalpha()])
    pals = set()
    for p in permutations(letters):
        pal = ''.join(p)
        if pal == pal[::-1] and len(pal) >= 4:
            pals.add(pal)
    return pals