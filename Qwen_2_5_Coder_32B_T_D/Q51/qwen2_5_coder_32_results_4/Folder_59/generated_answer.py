from collections import defaultdict

def if_contains_anagrams(lst):
    count = 0
    anagrams = defaultdict(list)
    for s in lst:
        s_cleaned = ''.join(sorted(s.lower()))
        if len(s_cleaned) >= 3:
            anagrams[s_cleaned].append(s)
    for a in anagrams.values():
        count += len(a) * (len(a) - 1) // 2
        if count > 15:
            return False
    return True