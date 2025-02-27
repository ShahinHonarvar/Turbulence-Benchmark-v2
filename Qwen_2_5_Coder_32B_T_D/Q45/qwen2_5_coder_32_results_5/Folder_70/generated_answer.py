from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    a = s[1:7].lower()
    c = Counter(a)
    letters = ''.join([l * (c[l] // 2) for l in c if c[l] > 1])
    res = set()
    for p in permutations(letters):
        half = ''.join(p)
        if len(half) >= 2:
            full = half + ('' if len(half) * 2 == len(a) else min([l for l in c if c[l] % 2 == 1])) + half[::-1]
            res.add(full)
    return {p for p in res if len(p) >= 4}