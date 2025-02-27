def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()
        return len(word1) == len(word2) and sorted(word1) == sorted(word2)
    anagram_counts = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_counts[sorted_word] = anagram_counts.get(sorted_word, 0) + 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) <= 65