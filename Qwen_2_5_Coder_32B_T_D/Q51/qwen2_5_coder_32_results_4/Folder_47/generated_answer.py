from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(int)
    for s in lst:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            d[s] += 1
    count = 0
    for v in d.values():
        count += v * (v - 1) // 2
    return count <= 366