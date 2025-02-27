from collections import defaultdict

def if_contains_anagrams(words):
    word_dict = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            word_dict[sorted_word].append(word)
    anagram_pairs = 0
    for word_list in word_dict.values():
        if len(word_list) > 1:
            anagram_pairs += len(word_list) * (len(word_list) - 1) // 2
    return anagram_pairs >= 10