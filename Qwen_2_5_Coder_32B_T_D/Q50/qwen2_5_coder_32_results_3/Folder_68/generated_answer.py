from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            anagrams[''.join(sorted(s_lower))].append(s_lower)
    count = sum((1 for a in anagrams.values() if len(a) > 1))
    return count >= 9