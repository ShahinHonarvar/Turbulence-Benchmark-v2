from itertools import combinations
    from collections import Counter

def if_contains_anagrams(lst):
    a = [Counter(s.lower()) for s in lst if len(s) >= 3]
    return sum((1 for x, y in combinations(a, 2) if x == y)) >= 70