from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(s):
    t = s[3:9].lower()
    letters = [c for c in t if c in ascii_lowercase]
    p = set()
    for r in range(4, len(letters) + 1):
        for comb in permutations(letters, r):
            candidate = ''.join(comb)
            if candidate == candidate[::-1]:
                p.add(candidate)
    return p