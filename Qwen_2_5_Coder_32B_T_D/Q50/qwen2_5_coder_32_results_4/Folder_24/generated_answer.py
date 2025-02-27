from collections import defaultdict

def if_contains_anagrams(lst):
    a = defaultdict(list)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            a[''.join(sorted(s_lower))].append(s_lower)
    count = sum((len(v) * (len(v) - 1) // 2 for v in a.values() if len(v) > 1))
    return count >= 65