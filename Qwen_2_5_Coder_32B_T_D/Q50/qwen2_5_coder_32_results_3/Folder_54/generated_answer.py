from collections import Counter

def if_contains_anagrams(lst):
    count = Counter((''.join(sorted(s.lower())) for s in lst if len(s) >= 3))
    pairs = sum((n * (n - 1) // 2 for n in count.values()))
    return pairs >= 74