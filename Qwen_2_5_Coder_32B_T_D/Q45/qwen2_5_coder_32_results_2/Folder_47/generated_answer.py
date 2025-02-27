from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:8])).lower()
    seen = set()
    for perm in permutations(letters):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 5:
            seen.add(p)
    return seen