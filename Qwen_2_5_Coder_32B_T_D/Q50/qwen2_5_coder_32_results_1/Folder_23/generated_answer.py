from collections import Counter, defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            d[tuple(sorted(s))] += 1
    count = 0
    for v in d.values():
        if v > 1:
            count += v * (v - 1) // 2
    return count >= 67