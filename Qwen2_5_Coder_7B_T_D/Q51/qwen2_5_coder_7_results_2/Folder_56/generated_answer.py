from collections import Counter

def if_contains_anagrams(words):
    anagram_pairs = 0
    word_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3 and sorted_word in word_dict:
            anagram_pairs += 1
        else:
            word_dict[sorted_word] = 1
    return anagram_pairs <= 11