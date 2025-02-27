from collections import defaultdict

def if_contains_anagrams(words):
    anagram_counts = defaultdict(int)
    threshold = 75

    def normalize(word):
        return ''.join(sorted(word.lower()))
    for word in words:
        if len(word) >= 3:
            normalized_word = normalize(word)
            anagram_counts[normalized_word] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs >= threshold