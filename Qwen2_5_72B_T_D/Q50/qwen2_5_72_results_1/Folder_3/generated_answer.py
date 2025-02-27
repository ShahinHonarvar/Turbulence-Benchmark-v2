from collections import Counter

def if_contains_anagrams(strings):
    normalized = [''.join(sorted(word.lower())) for word in strings if len(word) >= 3]
    count = Counter(normalized)
    pairs = sum((v * (v - 1) // 2 for v in count.values()))
    return pairs >= 30