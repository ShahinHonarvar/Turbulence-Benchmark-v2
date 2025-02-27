from collections import defaultdict

def if_contains_anagrams(lst):
    cnt = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            cnt[''.join(sorted(s))] += 1
    pairs = sum((c * (c - 1) // 2 for c in cnt.values() if c > 1))
    return pairs <= 289