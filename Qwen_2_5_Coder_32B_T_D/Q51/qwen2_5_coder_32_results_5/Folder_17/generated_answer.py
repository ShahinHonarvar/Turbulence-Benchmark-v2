from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = defaultdict(int)
    for word in words:
        word_sorted = ''.join(sorted(word.lower()))
        if len(word_sorted) >= 3:
            anagram_count[word_sorted] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return pairs <= 22