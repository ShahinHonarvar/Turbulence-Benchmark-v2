from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            d[''.join(sorted(s))].append(s)
    count = 0
    for anagrams in d.values():
        count += len(list(combinations(anagrams, 2)))
        if count > 279:
            return False
    return True