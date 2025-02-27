from collections import defaultdict

def if_contains_anagrams(lst):
    s = defaultdict(int)
    for w in lst:
        w = w.lower()
        if len(w) >= 3:
            s[''.join(sorted(w))] += 1
    c = sum((v * (v - 1) // 2 for v in s.values()))
    return c <= 41