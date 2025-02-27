from collections import Counter

def if_contains_anagrams(words):
    anagram_pairs = 0
    word_counts = Counter()
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in word_counts:
                anagram_pairs += word_counts[sorted_word]
                word_counts[sorted_word] += 1
            else:
                word_counts[sorted_word] = 1
    return anagram_pairs <= 11