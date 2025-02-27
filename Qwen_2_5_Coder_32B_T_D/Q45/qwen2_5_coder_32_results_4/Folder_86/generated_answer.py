from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[6:10] if c.isalpha()]
    p = set()
    for perm in permutations(letters):
        x = ''.join(perm)
        if x == x[::-1] and len(x) >= 4:
            p.add(x)
    return p