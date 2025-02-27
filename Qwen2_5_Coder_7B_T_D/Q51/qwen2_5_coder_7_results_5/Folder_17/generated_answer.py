from collections import Counter

def if_contains_anagrams(words):
    anagram_pairs = 0
    word_count = Counter()
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            word_count[sorted_word] += 1
            if word_count[sorted_word] > 2:
                anagram_pairs += word_count[sorted_word] - 2
    return anagram_pairs <= 22