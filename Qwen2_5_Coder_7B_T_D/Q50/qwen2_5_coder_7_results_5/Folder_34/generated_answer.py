def if_contains_anagrams(words):
    word_map = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in word_map:
                word_map[sorted_word].append(word)
            else:
                word_map[sorted_word] = [word]
    anagram_pairs = 0
    for key in word_map:
        if len(word_map[key]) > 1:
            anagram_pairs += len(word_map[key]) * (len(word_map[key]) - 1) // 2
    return anagram_pairs >= 25