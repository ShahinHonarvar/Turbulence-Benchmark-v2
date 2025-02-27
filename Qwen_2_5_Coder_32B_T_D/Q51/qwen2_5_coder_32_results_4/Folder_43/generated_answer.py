from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        s_sorted = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagrams[s_sorted].append(s)
    count = sum((1 for v in anagrams.values() if len(v) > 1))
    return count <= 3