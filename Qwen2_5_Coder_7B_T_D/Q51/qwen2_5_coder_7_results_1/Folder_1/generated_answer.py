from collections import Counter

def if_contains_anagrams(words):
    word_count = Counter()
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            word_count[sorted_word] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in word_count.values() if v > 1))
    return anagram_pairs <= 30