from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            s = ''.join(sorted(s))
            anagrams[s] += 1
    count = sum((v * (v - 1) // 2 for v in anagrams.values()))
    return count <= 61