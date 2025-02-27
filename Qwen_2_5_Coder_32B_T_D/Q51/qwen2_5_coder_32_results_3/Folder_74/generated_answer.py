from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(int)
    for s in lst:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagrams[s] += 1
    count = 0
    for v in anagrams.values():
        count += v * (v - 1) // 2
    return count <= 57