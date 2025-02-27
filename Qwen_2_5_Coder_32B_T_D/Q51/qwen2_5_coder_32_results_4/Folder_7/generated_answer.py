from itertools import combinations
    from collections import Counter

def if_contains_anagrams(lst):
    s = [Counter(sorted(s.lower())) for s in lst if len(s) >= 3]
    c = sum((1 for a, b in combinations(s, 2) if a == b))
    return c <= 445