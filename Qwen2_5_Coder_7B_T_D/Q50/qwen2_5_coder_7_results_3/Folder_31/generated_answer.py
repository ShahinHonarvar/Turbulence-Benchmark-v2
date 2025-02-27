from collections import defaultdict

def if_contains_anagrams(lst):
    counts = defaultdict(int)
    for s in lst:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            counts[sorted_s] += 1
    pairs = sum((v * (v - 1) // 2 for v in counts.values()))
    return pairs >= 68