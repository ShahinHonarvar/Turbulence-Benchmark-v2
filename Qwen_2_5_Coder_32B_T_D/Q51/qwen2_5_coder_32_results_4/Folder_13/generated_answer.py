from itertools import combinations
    from collections import Counter

def if_contains_anagrams(words):
    a = Counter((''.join(sorted(w.lower())) for w in words if len(w) >= 3))
    return sum((v * (v - 1) // 2 for v in a.values())) <= 54