from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            anagrams[sorted_s].append(s)
    count = 0
    for group in anagrams.values():
        count += len(group) * (len(group) - 1) // 2
        if count > 8:
            return False
    return True