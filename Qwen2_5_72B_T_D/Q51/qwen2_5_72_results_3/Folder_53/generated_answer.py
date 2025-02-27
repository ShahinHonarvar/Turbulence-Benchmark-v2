from collections import Counter

def if_contains_anagrams(strings):
    normalized = [''.join(sorted(word.lower())) for word in strings if len(word) >= 3]
    anagram_counts = Counter(normalized)
    pairs_of_anagrams = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs_of_anagrams <= 8