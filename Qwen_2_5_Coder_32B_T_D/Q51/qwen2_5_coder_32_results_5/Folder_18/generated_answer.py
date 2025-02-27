from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(lst):
    cnt = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            s = ''.join(sorted(s))
            cnt[s] += 1
    pairs = sum((c * (c - 1) // 2 for c in cnt.values()))
    return pairs <= 42