from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            anagrams[''.join(sorted(s_lower))].append(s_lower)
    pairs = 0
    for group in anagrams.values():
        pairs += len(group) * (len(group) - 1) // 2
    return pairs >= 219