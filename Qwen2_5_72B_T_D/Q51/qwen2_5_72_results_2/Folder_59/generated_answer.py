from collections import Counter

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = Counter()
    for word in words:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            anagram_counts[normalized_word] += 1
    anagram_pairs = sum((count - 1 for count in anagram_counts.values() if count > 1))
    return anagram_pairs <= 15