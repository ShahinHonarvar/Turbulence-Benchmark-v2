from collections import Counter

def if_contains_anagrams(lst):
    normalized = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    anagram_counts = Counter(normalized)
    anagram_pairs = sum((count >= 2 for count in anagram_counts.values()))
    return anagram_pairs >= 2