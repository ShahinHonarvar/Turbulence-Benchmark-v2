def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def count_anagrams(word_list):
        word_dict = {}
        for word in word_list:
            if len(word) >= 3:
                word_dict[word] = word_dict.get(word, 0) + 1
        anagram_pairs = 0
        for count in word_dict.values():
            if count > 1:
                anagram_pairs += count * (count - 1) // 2
        return anagram_pairs
    return count_anagrams(words) >= 77