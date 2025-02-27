from collections import defaultdict

def if_contains_anagrams(words_list):

    def are_anagrams(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    anagrams_count = 0
    word_dict = defaultdict(list)
    for word in words_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            word_dict[sorted_word].append(word.lower())
    for anagrams in word_dict.values():
        for i, first_word in enumerate(anagrams):
            for second_word in anagrams[i + 1:]:
                if are_anagrams(first_word, second_word):
                    anagrams_count += 1
                    if anagrams_count > 116:
                        return False
    return True