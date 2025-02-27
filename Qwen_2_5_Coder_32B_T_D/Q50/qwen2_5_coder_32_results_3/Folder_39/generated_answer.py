from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(int)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = tuple(sorted(s_lower))
            anagrams[sorted_s] += 1
    count = sum((v * (v - 1) // 2 for v in anagrams.values() if v > 1))
    return count >= 54