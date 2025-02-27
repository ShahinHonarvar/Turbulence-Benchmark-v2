from itertools import combinations

def if_contains_anagrams(words):

    def are_anagrams(word1, word2):
        return sorted(word1) == sorted(word2)
    words = [word.lower() for word in words if len(word) >= 3]
    anagram_count = sum((are_anagrams(word1, word2) for word1, word2 in combinations(words, 2)))
    return anagram_count <= 42