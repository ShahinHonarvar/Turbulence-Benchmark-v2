from itertools import combinations

def if_contains_anagrams(words):

    def are_anagrams(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    anagram_count = 0
    for word1, word2 in combinations(words, 2):
        if len(word1) >= 3 and len(word2) >= 3 and are_anagrams(word1, word2):
            anagram_count += 1
            if anagram_count > 65:
                return False
    return True