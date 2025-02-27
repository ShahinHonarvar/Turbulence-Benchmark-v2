from itertools import combinations

def if_contains_anagrams(words):

    def are_anagrams(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    valid_pairs = 0
    for word1, word2 in combinations(words, 2):
        if len(word1) >= 3 and len(word2) >= 3 and are_anagrams(word1, word2):
            valid_pairs += 1
    return valid_pairs <= 77