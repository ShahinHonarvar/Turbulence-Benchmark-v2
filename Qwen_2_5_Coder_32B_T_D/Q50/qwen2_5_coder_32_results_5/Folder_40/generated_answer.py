from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for s in lst:
        key = tuple(sorted(s.lower()))
        if len(s) >= 3:
            d[key].append(s)
    count = sum((1 for k in d if len(d[k]) > 1))
    return count >= 3