from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:8] if c.isalpha()]
    seen = set()
    for perm in permutations(letters):
        p = ''.join(perm)
        if len(p) >= 7 and p == p[::-1]:
            seen.add(p)
    return seen