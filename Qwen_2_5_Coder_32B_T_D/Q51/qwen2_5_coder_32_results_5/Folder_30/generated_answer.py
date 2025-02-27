from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            d[''.join(sorted(s))] += 1
    pairs = 0
    for count in d.values():
        pairs += count * (count - 1) // 2
        if pairs > 28:
            return False
    return True