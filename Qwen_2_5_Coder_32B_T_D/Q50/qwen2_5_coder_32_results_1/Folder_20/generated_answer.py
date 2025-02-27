from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            d[''.join(sorted(s))].append(s)
    count = sum((len(v) * (len(v) - 1) // 2 for v in d.values() if len(v) > 1))
    return count >= 64