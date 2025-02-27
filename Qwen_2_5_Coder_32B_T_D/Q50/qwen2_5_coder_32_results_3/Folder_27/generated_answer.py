from itertools import combinations
    from collections import Counter

def if_contains_anagrams(words):
    s = set()
    for word in words:
        w = word.lower()
        if len(w) >= 3:
            s.add(tuple(sorted(w)))
    c = Counter(s)
    pairs = sum((v * (v - 1) // 2 for v in c.values()))
    return pairs >= 86