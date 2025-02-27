def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]) and len(words[i]) >= 3:
                anagram_pairs += 1
                if anagram_pairs >= 3:
                    return True
    return False