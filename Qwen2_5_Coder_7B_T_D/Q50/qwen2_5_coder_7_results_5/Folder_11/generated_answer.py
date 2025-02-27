def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    word_count = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in word_count:
                word_count[sorted_word] += 1
            else:
                word_count[sorted_word] = 1
    anagram_pairs = sum([v * (v - 1) // 2 for v in word_count.values() if v > 1])
    return anagram_pairs >= 28