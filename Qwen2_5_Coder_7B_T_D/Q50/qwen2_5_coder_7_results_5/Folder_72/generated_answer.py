from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagrams[sorted_s].append(s)
    pairs = 0
    for s in anagrams.values():
        if len(s) > 1:
            pairs += len(s) * (len(s) - 1) // 2
    return pairs >= 55