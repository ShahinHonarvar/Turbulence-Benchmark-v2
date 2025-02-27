from collections import defaultdict

def if_contains_anagrams(lst):
    counts = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            counts[''.join(sorted(s))] += 1
    pairs = sum((v * (v - 1) // 2 for v in counts.values()))
    return pairs >= 78