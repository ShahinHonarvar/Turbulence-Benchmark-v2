from collections import Counter

def if_contains_anagrams(words):
    cnt = Counter((''.join(sorted(w.lower())) for w in words if len(w) >= 3))
    return sum((v * (v - 1) // 2 for v in cnt.values())) >= 411