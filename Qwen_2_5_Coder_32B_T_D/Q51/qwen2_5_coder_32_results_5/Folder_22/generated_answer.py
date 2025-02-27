from collections import defaultdict

def if_contains_anagrams(words):
    anagram_counts = defaultdict(int)
    for word in words:
        word_cleaned = ''.join(sorted(word.lower()))
        if len(word_cleaned) >= 3:
            anagram_counts[word_cleaned] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs <= 14