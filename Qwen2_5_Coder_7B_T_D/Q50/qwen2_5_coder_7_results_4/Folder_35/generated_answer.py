from collections import Counter

def if_contains_anagrams(words):
    word_counts = Counter()
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            word_counts[sorted_word] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in word_counts.values()))
    return anagram_pairs >= 153