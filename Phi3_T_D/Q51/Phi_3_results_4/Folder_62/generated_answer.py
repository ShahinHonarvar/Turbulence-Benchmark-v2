from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower()) and len(word1) >= 3
    anagram_pairs = 0
    seen_words = defaultdict(int)
    for word1 in words:
        for word2 in words:
            if word1.lower() != word2.lower() and is_anagram(word1, word2):
                seen_words[word1.lower()] += 1
                if seen_words[word1.lower()] == 1:
                    anagram_pairs += 1
    return anagram_pairs <= 289