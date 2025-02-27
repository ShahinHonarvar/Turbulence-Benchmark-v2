from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = tuple(sorted(s_lower))
            anagrams[sorted_s].append(s_lower)
    count = 0
    for group in anagrams.values():
        n = len(group)
        count += n * (n - 1) // 2
        if count >= 177:
            return True
    return False