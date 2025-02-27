from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[6:9])).lower()
    p = set()
    for perm in permutations(letters, len(letters)):
        pal = ''.join(perm)
        if pal == pal[::-1] and len(pal) >= 3:
            p.add(pal)
    return p