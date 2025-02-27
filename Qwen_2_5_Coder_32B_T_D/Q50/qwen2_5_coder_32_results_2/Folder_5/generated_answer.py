from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(int)
    for s in lst:
        s_sorted = ''.join(sorted(s.lower()))
        if len(s_sorted) >= 3:
            d[s_sorted] += 1
    pairs = sum((v * (v - 1) // 2 for v in d.values()))
    return pairs >= 21