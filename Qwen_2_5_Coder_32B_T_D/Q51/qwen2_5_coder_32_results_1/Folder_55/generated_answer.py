from collections import defaultdict

def if_contains_anagrams(lst):
    count = 0
    anagrams = defaultdict(list)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagrams[sorted_s].append(s_lower)
    for group in anagrams.values():
        count += len(group) * (len(group) - 1) // 2
        if count > 44:
            return False
    return True