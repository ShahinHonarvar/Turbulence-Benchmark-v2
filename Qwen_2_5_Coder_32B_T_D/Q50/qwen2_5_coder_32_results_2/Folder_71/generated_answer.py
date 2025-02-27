from itertools import combinations
    from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    lst = [s.lower() for s in lst if len(s) >= 3]
    for a, b in combinations(lst, 2):
        if Counter(a) == Counter(b):
            count += 1
    return count >= 57