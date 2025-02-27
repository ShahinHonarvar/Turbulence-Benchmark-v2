from collections import defaultdict

def if_contains_anagrams(lst):
    dd = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            dd[''.join(sorted(s))] += 1
    return sum((v * (v - 1) // 2 for v in dd.values() if v > 1)) >= 48