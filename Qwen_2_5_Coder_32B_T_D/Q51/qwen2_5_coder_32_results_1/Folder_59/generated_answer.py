from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(int)
    for s in lst:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            d[s] += 1
    return sum((v * (v - 1) // 2 for v in d.values())) <= 15