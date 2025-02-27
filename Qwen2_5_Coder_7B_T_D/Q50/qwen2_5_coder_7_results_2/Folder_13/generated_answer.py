def if_contains_anagrams(words):
    word_dict = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in word_dict:
                word_dict[sorted_word].append(word)
            else:
                word_dict[sorted_word] = [word]
    anagram_pairs = sum([len(v) * (len(v) - 1) // 2 for v in word_dict.values() if len(v) > 1])
    return anagram_pairs >= 144