def if_contains_anagrams(words):
    word_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word in word_dict:
                word_dict[sorted_word].append(word)
            else:
                word_dict[sorted_word] = [word]
    anagram_pairs = 0
    for key in word_dict:
        if len(word_dict[key]) > 1:
            anagram_pairs += len(word_dict[key]) * (len(word_dict[key]) - 1) // 2
    return anagram_pairs <= 60