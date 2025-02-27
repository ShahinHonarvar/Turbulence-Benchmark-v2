from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagrams[sorted_s].append(s)
    for v in anagrams.values():
        if len(v) >= 2:
            pairs = len(v) * (len(v) - 1) // 2
            if pairs >= 9:
                return True
    return False