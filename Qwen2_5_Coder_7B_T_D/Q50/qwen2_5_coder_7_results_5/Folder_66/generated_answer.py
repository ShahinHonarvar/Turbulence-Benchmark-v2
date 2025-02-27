def if_contains_anagrams(words):
    word_map = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in word_map:
                word_map[sorted_word] += 1
            else:
                word_map[sorted_word] = 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in word_map.values() if count > 1))
    return anagram_pairs >= 92