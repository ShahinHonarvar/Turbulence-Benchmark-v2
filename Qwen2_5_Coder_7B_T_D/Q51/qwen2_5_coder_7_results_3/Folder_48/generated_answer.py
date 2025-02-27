from collections import Counter

def if_contains_anagrams(str_list):
    anagram_count = 0
    word_dict = {}
    for word in str_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in word_dict:
                word_dict[sorted_word] += 1
            else:
                word_dict[sorted_word] = 1
    for count in word_dict.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count <= 277