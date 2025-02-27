from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(int)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            d[''.join(sorted(s_lower))] += 1
    count = sum((v * (v - 1) // 2 for v in d.values() if v > 1))
    return count >= 178