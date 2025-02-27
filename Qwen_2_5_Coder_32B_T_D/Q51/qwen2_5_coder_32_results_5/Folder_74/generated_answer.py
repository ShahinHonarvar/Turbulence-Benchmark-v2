from collections import Counter

def if_contains_anagrams(words):
    word_counts = Counter((''.join(sorted(word.lower())) for word in words if len(word) >= 3))
    anagram_pairs = sum((v * (v - 1) // 2 for v in word_counts.values()))
    return anagram_pairs <= 57