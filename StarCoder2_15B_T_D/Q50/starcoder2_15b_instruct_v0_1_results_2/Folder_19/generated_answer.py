def if_contains_anagrams(words):

    def anagrams(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower()) and len(word1) >= 3
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if anagrams(words[i], words[j]):
                anagram_pairs += 1
    return anagram_pairs >= 84