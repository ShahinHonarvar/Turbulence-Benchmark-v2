from collections import Counter

def if_contains_anagrams(words):

    def are_anagrams(word1, word2):
        return Counter(word1) == Counter(word2)
    words = [word.lower() for word in words if len(word) >= 3 and word.isalpha()]
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if are_anagrams(words[i], words[j]):
                anagram_pairs += 1
    return anagram_pairs <= 279