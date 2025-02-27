from collections import defaultdict

def if_contains_anagrams(l):
    d = defaultdict(int)
    for s in l:
        s = s.lower()
        if len(s) >= 3:
            d[''.join(sorted(s))] += 1
    c = sum((v * (v - 1) // 2 for v in d.values() if v > 1))
    return c <= 20