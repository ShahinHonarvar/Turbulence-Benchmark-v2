from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagrams[sorted_s].append(s_lower)
    count = 0
    for v in anagrams.values():
        if len(v) >= 2:
            count += len(v) // 2
    return count >= 4