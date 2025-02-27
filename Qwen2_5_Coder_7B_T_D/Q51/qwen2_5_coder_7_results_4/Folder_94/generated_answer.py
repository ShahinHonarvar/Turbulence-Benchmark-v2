def if_contains_anagrams(words):
    word_dict = {}
    for word in words:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            if sorted_word in word_dict:
                word_dict[sorted_word] += 1
            else:
                word_dict[sorted_word] = 1
    anagram_pairs = sum((value * (value - 1) // 2 for value in word_dict.values() if value > 1))
    return anagram_pairs <= 181