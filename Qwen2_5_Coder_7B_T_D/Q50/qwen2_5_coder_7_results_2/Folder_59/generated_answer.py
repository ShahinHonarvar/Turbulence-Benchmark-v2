from collections import Counter

def if_contains_anagrams(words):

    def sorted_chars(word):
        return sorted(word.lower())
    word_map = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = sorted_chars(word)
            if sorted_word in word_map:
                word_map[sorted_word].append(word)
            else:
                word_map[sorted_word] = [word]
    anagram_pairs = 0
    for key, value in word_map.items():
        if len(value) > 1:
            anagram_pairs += len(value) * (len(value) - 1) // 2
    return anagram_pairs >= 10