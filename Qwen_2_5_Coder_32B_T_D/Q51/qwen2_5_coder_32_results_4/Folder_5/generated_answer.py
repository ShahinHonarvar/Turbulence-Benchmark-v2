from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(int)
    for s in lst:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            d[s] += 1
    count = sum((v // 2 for v in d.values() if v > 1))
    return count <= 4