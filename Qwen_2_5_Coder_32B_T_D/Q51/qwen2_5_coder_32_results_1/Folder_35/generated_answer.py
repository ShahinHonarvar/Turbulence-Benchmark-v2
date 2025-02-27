from itertools import combinations
    from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    processed_words = [Counter(word.lower()) for word in lst if len(word) >= 3]
    for word1, word2 in combinations(processed_words, 2):
        if word1 == word2:
            anagram_count += 1
            if anagram_count > 210:
                return False
    return True