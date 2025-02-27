from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(int)
    for s in lst:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagrams[s] += 1
    pair_count = sum((v * (v - 1) // 2 for v in anagrams.values()))
    return pair_count <= 75