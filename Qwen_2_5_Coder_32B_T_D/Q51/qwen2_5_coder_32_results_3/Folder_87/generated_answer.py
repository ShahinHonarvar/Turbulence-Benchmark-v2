from itertools import combinations
    from collections import Counter

def if_contains_anagrams(lst):
    lst = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3]
    count = sum((1 for a, b in combinations(lst, 2) if a == b))
    return count <= 392