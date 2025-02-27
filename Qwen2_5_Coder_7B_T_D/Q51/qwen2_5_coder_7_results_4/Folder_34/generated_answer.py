from collections import Counter

def if_contains_anagrams(words):
    anagram_count = 0
    word_set = set()
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) < 3:
            continue
        if sorted_word in word_set:
            anagram_count += word_set[sorted_word]
        word_set[sorted_word] = word_set.get(sorted_word, 0) + 1
    return anagram_count <= 401