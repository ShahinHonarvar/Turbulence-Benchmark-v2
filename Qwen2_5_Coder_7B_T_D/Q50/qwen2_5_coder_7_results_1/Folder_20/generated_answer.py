def if_contains_anagrams(words):
    word_map = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3 and sorted_word in word_map:
            word_map[sorted_word] += 1
        elif len(word) >= 3:
            word_map[sorted_word] = 1
    anagram_pairs = sum([v * (v - 1) // 2 for v in word_map.values() if v > 1])
    return anagram_pairs >= 64