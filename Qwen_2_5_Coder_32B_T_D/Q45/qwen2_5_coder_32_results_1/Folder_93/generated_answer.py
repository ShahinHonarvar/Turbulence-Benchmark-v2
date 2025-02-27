from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:8])).lower()
    seen = set()
    for perm in permutations(letters, len(letters)):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 6:
            seen.add(p)
    return seen