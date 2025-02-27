from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            anagrams[sorted_s].append(s)
    pairs = 0
    for group in anagrams.values():
        if len(group) > 1:
            pairs += len(group) * (len(group) - 1) // 2
    return pairs >= 20