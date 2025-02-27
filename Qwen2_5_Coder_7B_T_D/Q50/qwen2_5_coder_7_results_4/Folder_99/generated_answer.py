from collections import defaultdict

def if_contains_anagrams(words):
    word_counts = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            word_counts[sorted_word] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in word_counts.values() if v > 1))
    return anagram_pairs >= 314