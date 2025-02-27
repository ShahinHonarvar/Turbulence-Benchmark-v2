from collections import Counter

def if_contains_anagrams(lst):
    count = Counter([''.join(sorted(s.lower())) for s in lst if len(s) >= 3])
    pairs = sum((v * (v - 1) // 2 for v in count.values() if v > 1))
    return pairs >= 43