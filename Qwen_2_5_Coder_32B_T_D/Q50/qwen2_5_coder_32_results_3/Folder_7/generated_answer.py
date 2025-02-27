from itertools import combinations
    from collections import Counter

def if_contains_anagrams(lst):
    s = [Counter(w.lower()) for w in lst if len(w) >= 3]
    return sum((1 for a, b in combinations(s, 2) if a == b)) >= 178