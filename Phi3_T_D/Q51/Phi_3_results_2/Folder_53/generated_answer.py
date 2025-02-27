from collections import defaultdict

def if_contains_anagrams(words):

    def hasAnagrams(word1, word2):
        if len(word1) < 3 or len(word2) < 3:
            return False
        word1, word2 = (word1.lower(), word2.lower())
        return sorted(word1) == sorted(word2)
    anagram_counts = defaultdict(int)
    for word1 in words:
        for word2 in words:
            if hasAnagrams(word1, word2):
                anagram_counts[word1] += 1
    return sum(anagram_counts.values()) // 2 <= 8