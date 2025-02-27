from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = defaultdict(int)
    for word in words:
        word_sorted = tuple(sorted(word.lower()))
        if len(word) >= 3:
            anagram_count[word_sorted] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_count.values() if v > 1))
    return pairs >= 39