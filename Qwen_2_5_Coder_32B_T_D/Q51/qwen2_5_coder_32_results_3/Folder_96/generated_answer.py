from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        key = tuple(sorted(s.lower()))
        if len(s) >= 3:
            anagrams[key].append(s)
    count = sum((1 for a in anagrams.values() if len(a) > 1))
    return count <= 2