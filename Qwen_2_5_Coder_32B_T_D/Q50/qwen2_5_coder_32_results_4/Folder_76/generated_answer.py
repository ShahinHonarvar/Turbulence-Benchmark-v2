from itertools import combinations
    from collections import defaultdict

def if_contains_anagrams(lst):
    s = defaultdict(int)
    for w in lst:
        w = w.lower()
        if len(w) >= 3:
            s[''.join(sorted(w))] += 1
    c = 0
    for v in s.values():
        if v > 1:
            c += v * (v - 1) // 2
    return c >= 143