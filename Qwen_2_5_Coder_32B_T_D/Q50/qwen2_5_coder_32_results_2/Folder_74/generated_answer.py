from collections import Counter

def if_contains_anagrams(strings):
    count = Counter((''.join(sorted(s.lower())) for s in strings if len(s) >= 3))
    pairs = sum((c * (c - 1) // 2 for c in count.values()))
    return pairs >= 17