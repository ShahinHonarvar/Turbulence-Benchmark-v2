from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:6].lower()
    letters = [c for c in s if c.isalpha()]
    seen = set()
    for perm in permutations(letters):
        p = ''.join(perm)
        if len(p) >= 5 and p == p[::-1]:
            seen.add(p)
    return seen