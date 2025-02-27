from collections import Counter

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return Counter(word1.lower()) == Counter(word2.lower())
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3 and is_anagram(words[i], words[j]):
                anagram_pairs += 1
    return anagram_pairs >= 77