from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:9] if c.isalpha()]
    p = set()
    for perm in permutations(letters):
        pal = ''.join(perm)
        if len(pal) >= 4 and pal == pal[::-1]:
            p.add(pal)
    return p