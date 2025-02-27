from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(int)
    for s in lst:
        if len(s) >= 3:
            s = ''.join(sorted(s.lower()))
            d[s] += 1
    return max(d.values()) <= 26