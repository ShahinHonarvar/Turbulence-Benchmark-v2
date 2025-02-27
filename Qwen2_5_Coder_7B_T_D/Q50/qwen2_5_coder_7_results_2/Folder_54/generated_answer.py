def if_contains_anagrams(words):
    word_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 6:
            if sorted_word in word_dict:
                word_dict[sorted_word] += 1
            else:
                word_dict[sorted_word] = 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in word_dict.values()))
    return anagram_pairs >= 74