from collections import defaultdict

def if_contains_anagrams(s):
    a = defaultdict(int)
    for w in s:
        w = w.lower()
        if len(w) >= 3:
            a[''.join(sorted(w))] += 1
    c = sum((v * (v - 1) // 2 for v in a.values() if v > 1))
    return c >= 93