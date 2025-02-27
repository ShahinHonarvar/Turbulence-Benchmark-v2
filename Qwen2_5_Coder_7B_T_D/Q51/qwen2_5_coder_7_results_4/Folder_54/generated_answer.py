from collections import Counter

def if_contains_anagrams(words):
    anagram_pairs = 0
    word_map = {}
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in word_map:
            anagram_pairs += word_map[sorted_word]
            word_map[sorted_word] += 1
        else:
            word_map[sorted_word] = 1
    return anagram_pairs <= 39