from collections import defaultdict

def if_contains_anagrams(lst):
    c = defaultdict(list)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            c[''.join(sorted(s_lower))].append(s_lower)
    pairs = sum((len(v) * (len(v) - 1) // 2 for v in c.values() if len(v) > 1))
    return pairs >= 47