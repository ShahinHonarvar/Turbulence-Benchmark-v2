from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            d[''.join(sorted(s))].append(s)
    cnt = sum((len(v) > 1 for v in d.values()))
    return cnt >= 11