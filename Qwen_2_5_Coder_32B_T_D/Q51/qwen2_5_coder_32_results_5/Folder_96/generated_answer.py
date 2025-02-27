from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            d[sorted_s].append(s_lower)
    count = sum((1 for v in d.values() if len(v) > 1))
    return count <= 2