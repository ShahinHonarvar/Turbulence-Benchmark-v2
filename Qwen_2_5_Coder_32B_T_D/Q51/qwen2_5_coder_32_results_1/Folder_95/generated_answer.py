from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            anagrams[key].append(s)
    pair_count = sum((1 for l in anagrams.values() if len(l) > 1))
    return pair_count <= 6