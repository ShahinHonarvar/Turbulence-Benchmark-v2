from collections import defaultdict

def if_contains_anagrams(lst):
    count = defaultdict(int)
    for s in lst:
        s = ''.join(sorted(s.lower()))
        if len(s) > 2:
            count[s] += 1
    pairs = sum((c * (c - 1) // 2 for c in count.values()))
    return pairs <= 366