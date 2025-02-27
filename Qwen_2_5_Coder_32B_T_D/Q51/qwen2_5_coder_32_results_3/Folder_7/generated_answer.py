from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    h = Counter((''.join(sorted(s.lower())) for s in lst if len(s) >= 3))
    pairs = sum((v * (v - 1) // 2 for v in h.values()))
    return pairs <= 445