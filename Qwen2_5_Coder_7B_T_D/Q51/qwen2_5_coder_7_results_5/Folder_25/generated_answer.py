from itertools import combinations

def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    for word1, word2 in combinations(words, 2):
        if len(word1) >= 3 and len(word2) >= 3 and is_anagram(word1, word2):
            anagram_pairs += 1
        if anagram_pairs > 67:
            return False
    return True