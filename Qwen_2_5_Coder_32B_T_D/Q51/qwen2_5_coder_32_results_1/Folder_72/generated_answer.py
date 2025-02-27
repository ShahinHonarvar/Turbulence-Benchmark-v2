from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(lst):
    count = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            count[''.join(sorted(s))] += 1
    pairs = sum((c * (c - 1) // 2 for c in count.values() if c > 1))
    return pairs <= 188