def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower()) and len(word1) >= 3 and (len(word2) >= 3)
    anagrams_count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                anagrams_count += 1
                if anagrams_count >= 4:
                    return True
    return False