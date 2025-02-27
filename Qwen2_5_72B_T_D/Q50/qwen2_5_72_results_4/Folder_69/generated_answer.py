from collections import Counter

def if_contains_anagrams(strings):
    normalized_sorted_words = [''.join(sorted(word.lower())) for word in strings if len(word) >= 3]
    count = Counter(normalized_sorted_words)
    anagram_pairs = sum((v * (v - 1) // 2 for v in count.values()))
    return anagram_pairs >= 188