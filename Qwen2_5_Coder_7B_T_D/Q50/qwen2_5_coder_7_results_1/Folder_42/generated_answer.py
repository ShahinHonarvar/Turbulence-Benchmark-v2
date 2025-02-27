from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            s = s.lower()
            d[''.join(sorted(s))].append(s)
    count = 0
    for k, v in d.items():
        if len(v) >= 2:
            count += len(v) * (len(v) - 1) // 2
    return count >= 233