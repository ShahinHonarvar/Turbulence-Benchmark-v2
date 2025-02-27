from itertools import combinations
    from collections import Counter

def if_contains_anagrams(lst):
    s = [Counter(x.lower()) for x in lst if len(x) >= 3]
    return sum((1 for a, b in combinations(s, 2) if a == b)) >= 64