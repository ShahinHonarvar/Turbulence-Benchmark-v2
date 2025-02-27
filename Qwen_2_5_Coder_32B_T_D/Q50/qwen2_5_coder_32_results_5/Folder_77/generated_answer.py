from itertools import combinations
    from collections import Counter

def if_contains_anagrams(lst):
    s = set()
    for word in lst:
        w = word.lower()
        if len(w) >= 3:
            s.add(''.join(sorted(w)))
    c = Counter(s)
    pairs = sum((v * (v - 1) // 2 for v in c.values() if v > 1))
    return pairs >= 209