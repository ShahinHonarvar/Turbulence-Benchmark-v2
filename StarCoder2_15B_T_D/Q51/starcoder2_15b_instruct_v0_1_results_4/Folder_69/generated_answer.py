def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    anagram_count = 0
    for i, word in enumerate(words):
        for j in range(i + 1, len(words)):
            if is_anagram(word, words[j]):
                anagram_count += 1
    return anagram_count <= 58