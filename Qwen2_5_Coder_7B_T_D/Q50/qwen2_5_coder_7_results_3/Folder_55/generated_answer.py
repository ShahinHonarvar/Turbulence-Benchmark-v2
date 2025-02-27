def if_contains_anagrams(lst):

    def get_sorted_word(word):
        return ''.join(sorted(word.lower()))
    word_dict = {}
    for word in lst:
        sorted_word = get_sorted_word(word)
        if len(word) >= 3:
            if sorted_word in word_dict:
                word_dict[sorted_word].append(word)
            else:
                word_dict[sorted_word] = [word]
    anagram_pairs = 0
    for words in word_dict.values():
        if len(words) > 1:
            anagram_pairs += len(words) * (len(words) - 1) // 2
    return anagram_pairs >= 15