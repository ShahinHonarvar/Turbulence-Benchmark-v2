from collections import defaultdict

def if_contains_anagrams(word_list):
    sorted_words = defaultdict(list)
    valid_words = 'abcdefghijklmnopqrstuvwxyz'
    anagram_pairs = 0
    for word in word_list:
        filtered_word = ''.join(filter(lambda x: x in valid_words, word.lower()))
        if len(filtered_word) >= 3:
            sorted_word = ''.join(sorted(filtered_word))
            sorted_words[sorted_word].append(word)
            anagram_pairs += len(sorted_words[sorted_word]) - 1
    return anagram_pairs <= 91