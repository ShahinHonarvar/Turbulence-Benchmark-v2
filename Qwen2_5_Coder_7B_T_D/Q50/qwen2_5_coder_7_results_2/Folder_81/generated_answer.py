from collections import Counter

def if_contains_anagrams(words):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    word_dict = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = sort_string(word)
            if sorted_word in word_dict:
                word_dict[sorted_word].append(word)
            else:
                word_dict[sorted_word] = [word]
    anagram_pairs = 0
    for key, value in word_dict.items():
        if len(value) > 1:
            anagram_pairs += len(value) * (len(value) - 1) // 2
    return anagram_pairs >= 16