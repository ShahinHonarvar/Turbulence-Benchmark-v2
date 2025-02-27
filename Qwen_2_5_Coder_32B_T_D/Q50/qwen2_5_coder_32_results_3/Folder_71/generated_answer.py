from itertools import combinations

def if_contains_anagrams(lst):
    d = {}
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = tuple(sorted(s_lower))
            d[sorted_s] = d.get(sorted_s, 0) + 1
    count = sum((v * (v - 1) // 2 for v in d.values()))
    return count >= 57