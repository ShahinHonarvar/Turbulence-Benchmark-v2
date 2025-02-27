from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagrams[sorted_s].append(s_lower)
    count = 0
    for group in anagrams.values():
        count += len(group) * (len(group) - 1) // 2
        if count >= 29:
            return True
    return False