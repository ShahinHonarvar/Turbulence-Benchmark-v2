from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(strings):
    count = 0
    anagrams = defaultdict(list)
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = tuple(sorted(s_lower))
            anagrams[sorted_s].append(s_lower)
    for group in anagrams.values():
        if len(group) > 1:
            count += len(list(combinations(group, 2)))
            if count >= 75:
                return True
    return False