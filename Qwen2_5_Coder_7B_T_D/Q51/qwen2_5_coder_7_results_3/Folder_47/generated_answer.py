def if_contains_anagrams(words):
    word_map = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in word_map:
                word_map[sorted_word] += 1
            else:
                word_map[sorted_word] = 1
    anagram_count = sum((value * (value - 1) // 2 for value in word_map.values()))
    return anagram_count <= 366