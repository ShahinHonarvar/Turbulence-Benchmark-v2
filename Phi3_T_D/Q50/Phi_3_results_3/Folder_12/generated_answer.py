from itertools import combinations

def if_contains_anagrams(word_list):

    def are_anagrams(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower()) and len(word1) >= 3 and (len(word2) >= 3)
    anagram_pairs_count = 0
    for word1, word2 in combinations(word_list, 2):
        if are_anagrams(word1, word2):
            anagram_pairs_count += 1
    return anagram_pairs_count >= 69