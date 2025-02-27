from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_word(word):
        return tuple(sorted(word.lower()))
    anagram_counts = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            anagram_counts[sorted_word(word)] += 1
    pair_count = sum((v * (v - 1) // 2 for v in anagram_counts.values()))
    return pair_count <= 289