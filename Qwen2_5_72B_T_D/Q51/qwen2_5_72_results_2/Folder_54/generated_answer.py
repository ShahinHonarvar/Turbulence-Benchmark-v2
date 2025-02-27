from collections import Counter

def if_contains_anagrams(lst):
    normalized = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    counter = Counter(normalized)
    pairs = sum((v * (v - 1) // 2 for v in counter.values()))
    return pairs <= 39