from itertools import combinations

def if_contains_anagrams(lst):
    s = set()
    for w in lst:
        sw = ''.join(sorted(w.lower()))
        if len(sw) >= 3:
            s.add(sw)
    pairs = sum((1 for a, b in combinations(s, 2) if a == b))
    return pairs <= 29