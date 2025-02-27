from collections import Counter

def if_contains_anagrams(lst):
    cnt = Counter((''.join(sorted(x.lower())) for x in lst if len(x) >= 3))
    pairs = sum((v * (v - 1) // 2 for v in cnt.values() if v > 1))
    return pairs >= 75