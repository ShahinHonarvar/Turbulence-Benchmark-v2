from collections import defaultdict

def if_contains_anagrams(lst):
    cnt = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            cnt[''.join(sorted(s))] += 1
    pairs = sum((v * (v - 1) // 2 for v in cnt.values()))
    return pairs >= 42