from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c for c in s[5:8].lower() if c.isalpha()])
    p = set()
    for perm in permutations(letters):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 4:
            p.add(candidate)
    return p