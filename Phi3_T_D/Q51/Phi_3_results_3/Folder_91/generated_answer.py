def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        word1, word2 = (word1.lower(), word2.lower())
        return len(word1) >= 3 and len(word2) >= 3 and (sorted(word1) == sorted(word2))
    count = sum((is_anagram(w1, w2) for i, w1 in enumerate(words) for w2 in words[i + 1:]))
    return count <= 88