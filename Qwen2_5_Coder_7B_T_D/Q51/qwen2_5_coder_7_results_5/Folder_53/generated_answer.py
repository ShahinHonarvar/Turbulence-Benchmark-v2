from collections import Counter

def if_contains_anagrams(words):
    word_dict = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in word_dict:
                word_dict[sorted_word] += 1
            else:
                word_dict[sorted_word] = 1
    anagram_pairs = sum([value // 2 for value in word_dict.values() if value > 1])
    return anagram_pairs <= 8