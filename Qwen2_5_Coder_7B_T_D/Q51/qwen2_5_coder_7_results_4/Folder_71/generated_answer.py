from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(int)
    for s in lst:
        if len(s) >= 3:
            count = ''.join(sorted(s.lower()))
            d[count] += 1
    pairs = sum(((v - 1) * v // 2 for v in d.values() if v > 1))
    return pairs <= 9