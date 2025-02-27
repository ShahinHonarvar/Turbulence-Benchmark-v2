from collections import Counter
    from itertools import permutations
    import string

def palindromes_between_indices(s):
    t = s[4:9].lower()
    c = Counter(t)
    letters = ''.join(c.elements())
    p = set()
    for perm in permutations(letters):
        w = ''.join(perm)
        if w == w[::-1] and len(w) >= 5:
            p.add(w)
    return p