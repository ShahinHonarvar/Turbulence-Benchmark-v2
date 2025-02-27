from collections import defaultdict

def if_contains_anagrams(words):
    d = defaultdict(int)
    for w in words:
        w = w.lower()
        if len(w) >= 3:
            d[''.join(sorted(w))] += 1
    pairs = sum((v * (v - 1) // 2 for v in d.values()))
    return pairs <= 86