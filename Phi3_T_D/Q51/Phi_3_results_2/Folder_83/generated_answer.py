from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s_lower = s.lower()
        key = tuple(sorted(s_lower))
        if len(s_lower) >= 3:
            anagrams[key] = anagrams.get(key, 0) + 1
    num_pairs = sum((v - 1 for v in anagrams.values())) // 2
    return num_pairs <= 19