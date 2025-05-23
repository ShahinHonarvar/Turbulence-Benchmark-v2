def if_contains_anagrams(words):
    word_map = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word in word_map:
                word_map[sorted_word] += 1
            else:
                word_map[sorted_word] = 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in word_map.values() if v > 1))
    return anagram_pairs >= 312