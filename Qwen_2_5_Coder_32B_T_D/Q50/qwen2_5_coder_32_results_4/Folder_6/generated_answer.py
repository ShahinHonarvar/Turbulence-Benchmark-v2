from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            d[''.join(sorted(s))] += 1
    return any((v >= 2 for v in d.values())) >= 26