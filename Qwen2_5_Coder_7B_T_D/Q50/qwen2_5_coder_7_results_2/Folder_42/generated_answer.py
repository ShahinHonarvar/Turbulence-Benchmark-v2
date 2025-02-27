from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagrams[sorted_s].append(s)
    return sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values())) >= 233