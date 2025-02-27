from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    t = s[5:8].lower()
    c = Counter(t)
    letters = ''.join([l * min(c[l], 2 if l * 2 != len(t) else 1) for l in c])
    p = set()
    for perm in permutations(letters):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 3:
            p.add(candidate)
    return p