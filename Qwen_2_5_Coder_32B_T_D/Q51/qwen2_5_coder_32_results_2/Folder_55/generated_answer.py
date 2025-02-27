from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(lst):
    cntr = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            cntr[''.join(sorted(s))] += 1
    pairs = sum((c * (c - 1) // 2 for c in cntr.values()))
    return pairs <= 44