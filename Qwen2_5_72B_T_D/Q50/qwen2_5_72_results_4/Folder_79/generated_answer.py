from collections import Counter

def if_contains_anagrams(lst):
    normalized = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    count = Counter(normalized)
    anagram_pairs = sum((c * (c - 1) // 2 for c in count.values()))
    return anagram_pairs >= 40