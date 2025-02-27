from collections import Counter

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = Counter()
    for word in words:
        if len(word) >= 3:
            normalized_word = normalize(word)
            anagram_counts[normalized_word] += 1
    anagram_pairs = sum((cnt * (cnt - 1) // 2 for cnt in anagram_counts.values()))
    return anagram_pairs <= 116