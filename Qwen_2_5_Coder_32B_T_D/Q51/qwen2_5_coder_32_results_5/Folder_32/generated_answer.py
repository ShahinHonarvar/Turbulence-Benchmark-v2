from collections import Counter

def if_contains_anagrams(words):
    s = [''.join(sorted(w.lower())) for w in words if len(w) >= 3]
    c = Counter(s)
    pairs = sum((v * (v - 1) // 2 for v in c.values()))
    return pairs <= 89