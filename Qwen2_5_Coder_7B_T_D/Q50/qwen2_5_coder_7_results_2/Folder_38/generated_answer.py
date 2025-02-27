def if_contains_anagrams(words):
    word_count = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word in word_count:
                word_count[sorted_word] += 1
            else:
                word_count[sorted_word] = 1
    anagram_pairs = sum((value * (value - 1) // 2 for value in word_count.values() if value > 1))
    return anagram_pairs >= 24