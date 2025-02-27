from collections import Counter

def if_contains_anagrams(strings):
    normalized = [''.join(sorted(word.lower())) for word in strings if len(word) >= 3]
    counts = Counter(normalized)
    pairs = sum((count * (count - 1) // 2 for count in counts.values()))
    return pairs >= 91