from collections import Counter

def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    anagram_pairs = 0
    words_set = set(words)
    for word1 in words_set:
        if len(word1) < 3:
            continue
        for word2 in words_set:
            if word1 < word2 and is_anagram(word1, word2):
                anagram_pairs += 1
    return anagram_pairs >= 34